/**
 * Copyright (c) 2017 MapR, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.mapr.ojai.examples;

import org.ojai.Document;
import org.ojai.DocumentStream;
import org.ojai.exceptions.QueryTimeoutException;
import org.ojai.store.Connection;
import org.ojai.store.DocumentStore;
import org.ojai.store.DriverManager;
import org.ojai.store.Query;

public class OJAI_013_ReadYourOwnWrite {

  public static void main(String[] args) {

    System.out.println("==== Start Application ===");


    // Create an OJAI connection to MapR cluster
    final Connection connectionNode1 = DriverManager.getConnection("ojai:mapr:");

    // Get an instance of OJAI DocumentStore
    final DocumentStore storeNode1 = connectionNode1.getStore("/demo_table");

    // initiate tracking of commit-context
    storeNode1.beginTrackingWrites();

    // issue a set of mutations/insert/delete/etc
    storeNode1.update("user0000", connectionNode1.newMutation().set("address.zipCode", 95110L));
    storeNode1.insertOrReplace(connectionNode1.newDocument(
        "{\"_id\": \"user0004\", \"name\": \"Jean Doe\", \"age\": 56, \"address\": {\"zipCode\":{\"$numberLong\":95110}}}"));

    final String commitContext = storeNode1.endTrackingWrites();

    // Close this instance of OJAI DocumentStore
    storeNode1.close();

    // close the OJAI connection and release any resources held by the connection
    connectionNode1.close();

    /*
     * Next section of the code can run on the same or on a different node,
     * the `commitContext` obtained earlier needs to be propagated to that node.
     */

    // Create an OJAI connection to MapR cluster
    final Connection connectionNode2 = DriverManager.getConnection("ojai:mapr:");

    // Get an instance of OJAI DocumentStore
    final DocumentStore storeNode2 = connectionNode2.getStore("/demo_table");

    // Build an OJAI query and set its commit context with timeout of 2 seconds
    final Query query = connectionNode2.newQuery()
        .select("_id", "name", "address.zipCode")
        .where("{\"$gt\": {\"address.zipCode\": 95110}}")
        .waitForTrackedWrites(commitContext)
        .build();

    try {
      // fetch all OJAI Documents from this store
      final DocumentStream stream = storeNode2.findQuery(query);
      for (final Document userDocument : stream) {
        // Print the OJAI Document
        System.out.println(userDocument.asJsonString());
      }
    } catch (QueryTimeoutException e) {
      System.err.println("Timeout occurred while waiting for Query results");
    }

    // Close this instance of OJAI DocumentStore
    storeNode2.close();

    // close the OJAI connection and release any resources held by the connection
    connectionNode2.close();

    System.out.println("==== End Application ===");
  }

}
