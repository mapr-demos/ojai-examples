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
import org.ojai.json.JsonOptions;
import org.ojai.store.Connection;
import org.ojai.store.DriverManager;

import com.mapr.ojai.examples.data.Dataset;
import com.mapr.ojai.examples.data.User;

public class OJAI_001_GetConnectionCreateDocument {

  public static void main(String[] args) {

    System.out.println("==== Start Application ===");


    // Create an OJAI connection to MapR cluster
    final Connection connection = DriverManager.getConnection("ojai:mapr:");

    for (final User someUser : Dataset.users) {
      // Create an OJAI Document form the Java bean (there are other ways too)
      final Document userDocument = connection.newDocument(someUser);

      // Print the OJAI Document
      System.out.println(
          userDocument.asJsonString(           // serialize the OJAI Document to JSON string
              new JsonOptions().pretty()       // in pretty format
      ));      
    }

    // close the OJAI connection and release any resources held by the connection
    connection.close();

    System.out.println("==== End Application ===");
  }

}
