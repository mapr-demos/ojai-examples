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

public class Dataset {

  // user data set
  public static final User[] users = {
    new User("user0000", 35, "John", "Doe",
        new Address("350 Hoger Way", "San Jose", "CA", 95134),
        new PhoneNumber[] {new PhoneNumber(555, 5555555), new PhoneNumber("555", "555-5556")}),

    new User("user0001", 26, "Jane", "Dupont",
        new Address("320 Blossom Hill Road", "San Jose", "CA", 95196),
        new PhoneNumber[] {new PhoneNumber(555, 5553827), new PhoneNumber("555", "555-6289")}),

    new User("user0002", 45, "Simon", "Davis",
        new Address("38 De Mattei Court", "San Jose", "CA", 95142),
        new PhoneNumber[] {new PhoneNumber(555, 5425639), new PhoneNumber("555", "542-5656")})
  };

}
