/*
 * Copyright (c) 2018 MapR, Inc.
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

const { ConnectionManager } = require('node-maprdb');

const connectionString = 'localhost:5678?' +
  'auth=basic;' +
  'user=mapr;' +
  'password=mapr;' +
  'ssl=true;' +
  'sslCA=/opt/mapr/conf/ssl_truststore.pem;' +
  'sslTargetNameOverride=node1.mapr.com';

let connection;
let store;
const docId = 'user0002';

// Create a connection to data access server
ConnectionManager.getConnection(connectionString)
  .then((conn) => {
    connection = conn;
    // Get a store
    return connection.getStore('/demo_table');
  })
  .then((newStore) => {
    // Get a store and assign it as a DocumentStore object
    store = newStore;
    // Find the document before update
    return store.findById(docId);
  })
  .then((docBeforeUpdate) => {
    // Print the document before update
    console.log(`Document with id ${docId} before update`)
    console.log(docBeforeUpdate);

    const mutation = {'$put': {'address.zipCode': 95196}};
    const condition = {'$eq': {'address.street': '320 Blossom Hill Road'}}
    return store.checkAndUpdate(docId, mutation, condition);
  })
  .then((updateResult) => {
    console.log(updateResult);
    // Find the document after update
    return store.findById(docId);
  })
  .then((docAfterUpdate) => {
    // Print the document after update
    console.log(`Document with id ${docId} before update`)
    console.log(docAfterUpdate);
  });
