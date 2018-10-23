# Getting Started with MapR-DB and OJAI 3.0

This project contains examples to discover the key features of OJAI 3.0 and MapR-DB JSON. 


**Prerequisites**

* MapR Converged Data Platform 6.1
* JDK 8
* Maven 3.0


## Build and Run the Sample Application


#### 1 - Create a new JSON Table

The sample application uses a JSON Table named `/demo_table`. Open a terminal window as mapr user and run the following command:
 
```
$ maprcli table create -path /demo_table -tabletype json
```

Optionally you can give access to this table to any user using the following command:

```
$ maprcli table cf edit -path /demo_table -cfname default -readperm p -writeperm p -traverseperm  p
```

#### 2 - Build and Deploy the Sample Application

Run the maven command to build the project:

```
$ mvn clean package
```

Copy the application jar to your MapR cluster, for example:

```
$ scp ./target/ojai-samples-1.0-SNAPSHOT.jar mapr@mapr61:/home/mapr/ 
```

Where `mapr61` is one of the node of the MapR cluster.


#### 3 - Run the Sample Application

In a terminal window, connected as mapr user type the following commands to run the various samples


```
$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_001_GetConnectionCreateDocument 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_002_GetStoreAndInsertDocuments 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_003_FindById 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_004_FindAll

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_005_FindAllQuery 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_006_FindQueryWithSelect 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_008_FindQueryWithConditionJson 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_009_FindQueryWithSelectAndCondition 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_010_FindQueryWithOrderBy

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_011_FindQueryWithOrderByLimitOffset 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_012_UpdateDocument 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_013_ReadYourOwnWrite 

$ java -cp ojai-samples-1.0-SNAPSHOT.jar:`mapr clientclasspath` com.mapr.ojai.examples.OJAI_014_FindQueryPlan 

```


#### 4- Run the application from the IDE (Optional)

The following steps are documented for MapR cluster where the secured mode has not been enabled.

**1- Create a MapR Client configuration file**

Create a file  `/opt/mapr/conf/mapr-clusters.conf`

Add the following configuration of your cluster in the file:

```
my.cluster.com secure=false mapr61:7222
```

Where:

* `my.cluster.com` is the name of your cluster
* `secure=false` specifies that the cluster secure mode is not enabled
* `mapr61:7222` is the host and port of the CLDB.

**2- Change the Table Permission**

In the previous step, the Java application is running as `mapr`, but when you are running the application from your IDE, the 
user that execute the Java application is your own user.

You need to change the permission of the default column family and create the same user id on the cluster to allow the application to be executed from the IDE or Maven.

```
$ maprcli table cf edit -path /demo_table -cfname default -readperm p -writeperm p -traverseperm  p
```

It is also possible to use MapR Control System to change the permission.


**3- Create a user on your cluster**

Note : The following step is a known limitation of MapR 6.0 Beta

In addition to this, you also need to create a user with the same login to allow the MapR-DB Query Service powered by Drill.

For example if your desktop user is "jdoe" with the id 501, create the user on your cluster nodes using for example:

```
# useradd -u 501 jdoe
```


**4- Run the sample applications**


```
$ mvn exec:java -Dexec.mainClass="com.mapr.ojai.examples.OJAI_011_FindQueryWithOrderByLimitOffset"
```




## Developing with OJAI and MapR DB

This project is an example allowing you to understand the key features of OJAI and MapR-DB; 
the following section explain the main steps to build your own project.


### Maven Dependencies

To use OJAI and MapR-DB you must add the MapR Maven Repository and the MapR OJAI Dependencies to your project

MapR Maven Repository

```xml
    <repository>
      <id>mapr-releases</id>
      <url>http://repository.mapr.com/maven/</url>
    </repository>

```

MapR-DB and OJAI Dependencies

```xml
    <dependency>
      <artifactId>mapr-ojai-driver</artifactId>
      <groupId>com.mapr.ojai</groupId>
      <version>6.0.0-mapr</version>
    </dependency>
```


### Using OJAI and MapR-DB API


**1- OJAI Connection**

The first thing to do when you want to use MapR-DB is to get an OJAI connection to the cluster using the following code:

```java
    // Create an OJAI connection to MapR cluster
    Connection connection = DriverManager.getConnection("ojai:mapr:");
	
```

This connection will use the MapR Client configuration to connect to the MapR Cluster

**2- Access a Document Store**

OJAI expose the MapR-DB JSON Tables as a DocumentStore that you get from the Connection object:

```java
    // Get an instance of OJAI DocumentStore
    DocumentStore store = connection.getStore("/demo_table");

```

The `/demo_table` is a path to a MapR-DB JSON Table that should exist.

**3- Create and insert a Document**

Use the `connection.newDocument()` method to create a new document from a String, Map, Java Bean or JSON Object.

Once the document is created use the 'store.insertOrUpdate()' method, or other, to insert the document in the table.

```java
    store.insertOrReplace(userDocument);
```



## Conclusion

This project shows the key features of OJAI 3.0 and how you can use the API to work with MapR-DB JSON:

* create and insert document
* update documents
* query document (projection, condition, sort and limit)

You also learned how to configure your development environment to run your MapR-DB/OJAI application from your desktop.

