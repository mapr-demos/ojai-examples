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

// Create a connection to data access server
ConnectionManager.getConnection(connectionString)
  .then((connection) => {
    // create new document as a JavaScript object
    const newDocument = {
      "_id": "id001",
      "name": "Joe",
      "age": 50,
      "address": {
        "street": "555 Moon Way",
        "city": "Gotham"
      }
    };

    // Print the OJAI Document
    console.log(JSON.stringify(newDocument));

    // close the OJAI connection and release any resources held by the connection
    connection.close();
  });
