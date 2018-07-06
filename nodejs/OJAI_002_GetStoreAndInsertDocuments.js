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

// Create a connection to data access server
ConnectionManager.getConnection(connectionString)
  .then((conn) => {
    connection = conn;
    // Get a store
    return connection.getStore('/demo_table');
  })
  .then((store) => {
    const documentList = [{'_id': 'user0000',
      'age': 35,
      'firstName': 'John',
      'lastName': 'Doe',
      'address': {
        'street': '350 Hoger Way',
        'city': 'San Jose',
        'state': 'CA',
        'zipCode': 95134
      },
      'phoneNumbers': [
        {'areaCode': 555, 'number': 5555555},
        {'areaCode': '555', 'number': '555-5556'}]
    },
      {'_id': 'user0001',
        'age': 26,
        'firstName': 'Jane',
        'lastName': 'Dupont',
        'address': {
          'street': '320 Blossom Hill Road',
          'city': 'San Jose',
          'state': 'CA',
          'zipCode': 95196
        },
        'phoneNumbers': [
          {'areaCode': 555, 'number': 5553827},
          {'areaCode': '555', 'number': '555-6289'}]
      },
      {'_id': 'user0002',
        'age': 45,
        'firstName': 'Simon',
        'lastName': 'Davis',
        'address': {
          'street': '38 De Mattei Court',
          'city': 'San Jose',
          'state': 'CA',
          'zipCode': 95142
        },
        'phoneNumbers': [
          {'areaCode': 555, 'number': 5425639},
          {'areaCode': '555', 'number': '542-5656'}]
      }
    ];
    const promiseList = documentList.map((doc) => {
      // Print the OJAI Document
      console.log(JSON.stringify(doc));
      // Insert the OJAI Document into the DocumentStore
      return store.insertOrReplace(doc);
    });
    return Promise.all(promiseList);
  })
  .then(() => {
    // close the OJAI connection
    connection.close();
  });
