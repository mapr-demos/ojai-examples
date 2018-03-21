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
package com.mapr.ojai.examples.data;

public final class User {
  public String _id;                    // the identifier of the objects
  public int age;                       // scalar field
  public String firstName;             // scalar field
  public String lastName;              // scalar field
  public Address address;               // complex field
  public PhoneNumber[] phoneNumbers;    // repeated, complex field

  public User(String _id, int age, String firstName, String lastName, Address address, PhoneNumber[] phoneNumbers) {
    this._id = _id;
    this.age = age;
    this.firstName = firstName;
    this.lastName = lastName;
    this.address = address;
    this.phoneNumbers = phoneNumbers;
  }

}