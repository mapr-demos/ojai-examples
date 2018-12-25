using System;
using MapRDB.Driver;

public class GetConnectionCreateDocument
{
    public void GetConnectionCreateDocument()
    {
        // Create a connection to data access server
        var connectionStr = $"localhost:5678?auth=basic;" +
            $"user=mapr;" +
            $"password=mapr;" +
            $"ssl=true;" +
            $"sslCA=/opt/mapr/conf/ssl_truststore.pem;" +
            $"sslTargetNameOverride=node1.mapr.com";
        var connection = ConnectionFactory.CreateConnection(connectionStr);

        // Json string
        var jsonStr =
            @"{" +
                @"""_id"":""id001""," +
                @"""name"":""Joe""," +
                @"""age"":{""$numberInt"":""50""}," +
                @"""address"":" +
                    @"{" +
                        @"""street"":""555 Moon Way""," +
                        @"""city"":""Gotham""" +
                    @"}" +
            @"}";

        // Create a document from jsonStr
        var documentJson = connection.NewDocument(jsonStr);

        // Print the OJAI Document
        Console.WriteLine(documentJson.ToJsonString());

        // Create new document with the same fields using constructor
        var documentConstructed = connection.NewDocument()
            .SetID("id001")
            .Set("name", "Joe")
            .Set("age", 50)
            .Set("address.street", "555 Moon Way")
            .Set("address.city", "Gotham");

        // Print the OJAI Document
        Console.WriteLine(documentConstructed.ToJsonString());

        // Close the OJAI connection
        connection.Close();
    }
}
