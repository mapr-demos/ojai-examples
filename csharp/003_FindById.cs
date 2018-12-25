using System;
using MapRDB.Driver;

public class FindById
{
    public void FindById()
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
        var store = connection.GetStore("/demo_table");

        // Fetch the OJAI Document by its '_id' field
        var document = store.FindById("user0001");

        // Print the OJAI Document
        Console.WriteLine(document);

        // Close the OJAI connection
        connection.Close();
    }
}
