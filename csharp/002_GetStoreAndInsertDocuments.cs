using System;
using MapRDB.Driver;
using System.Collections.Generic;

public class GetStoreAndInsertDocuments
{
	public void GetStoreAndInsertDocuments()
	{
        // Create a connection to data access server
        var connectionStr = $"localhost:5678?auth=basic;" +
            $"user=mapr;" +
            $"password=mapr;" +
            $"ssl=true;" +
            $"sslCA=/opt/mapr/conf/ssl_truststore.pem;" +
            $"sslTargetNameOverride=node1.mapr.com";
        var connection = ConnectionFactory.CreateConnection(connectionStr);

        // Get a store and assign it as a DocumentStore object
        if (!connection.StoreExist("/demo_table"))
            connection.CreateStore("/demo_table");
        var store = connection.GetStore("/demo_table");

        var documentList = new List<string>
            {
                @"{""_id"":""user0000""," +
                @"""age"":{""$numberInt"":""35""}," +
                @"""firstName"":""John""," +
                @"""lastName"":""Doe""," +
                @"""address"":{" +
                    @"""street"":""350 Hoger Way""," +
                    @"""city"":""San Jose""," +
                    @"""state"":""CA""," +
                    @"""zipCode"":{""$numberLong"":""95134""}" +
                    @"}," +
                @"""phoneNumbers"":[" +
                    @"{""areaCode"":{""$numberInt"":""555""},""number"":{""$numberLong"":""5555555""}}," +
                    @"{""areaCode"":""555"",""number"":""555-5556""}]" +
                @"}",
                @"{""_id"":""user0001""," +
                @"""age"":{""$numberInt"":""26""}," +
                @"""firstName"":""Jane""," +
                @"""lastName"":""Dupont""," +
                @"""address"":{" +
                    @"""street"":""320 Blossom Hill Road""," +
                    @"""city"":""San Jose""," +
                    @"""state"":""CA""," +
                    @"""zipCode"":{""$numberLong"":""95196""}" +
                    @"}," +
                @"""phoneNumbers"":[" +
                    @"{""areaCode"":{""$numberInt"":""555""},""number"":{""$numberLong"":""5553827""}}," +
                    @"{""areaCode"":""555"",""number"":""555-6289""}]" +
                @"}",
                @"{""_id"":""user0002""," +
                @"""age"":{""$numberInt"":""45""}," +
                @"""firstName"":""Simon""," +
                @"""lastName"":""Davis""," +
                @"""address"":{" +
                    @"""street"":""38 De Mattei Court""," +
                    @"""city"":""San Jose""," +
                    @"""state"":""CA""," +
                    @"""zipCode"":{""$numberLong"":""95142""}" +
                    @"}," +
                @"""phoneNumbers"":[" +
                    @"{""areaCode"":{""$numberInt"":""555""},""number"":{""$numberLong"":""5425639""}}," +
                    @"{""areaCode"":""555"",""number"":""542-5656""}]" +
                @"}"
            };

        foreach (var doc in documentList)
        {
            // Create new document from json string
            var document = connection.NewDocument(doc);

            // Print the OJAI Document
            Console.WriteLine(document.ToJsonString());

            // Insert the OJAI Document into the DocumentStore
            store.InsertOrReplace(document);
        }

        // Close the OJAI connection
        connection.Close();
    }
}
