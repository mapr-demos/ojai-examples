using System;
using MapRDB.Driver;

public class UpdateDocument
{
	public void UpdateDocument()
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

        var docId = "user0002";

        // Print the document before update
        var documentBeforeUpdate = store.FindById(docId);
        Console.WriteLine($"Document with id {docId} before update:");
        Console.WriteLine(documentBeforeUpdate);

        // Create mutation to update the zipCode field
        var mutation = connection.NewDocumentMutation().Set("address.zipCode", (long)95196);

        // Execute update
        store.Update(docId, mutation);

        // Print the document after update
        var documentAfterUpdate = store.FindById(docId);
        Console.WriteLine($"Document with id {docId} after update:");
        Console.WriteLine(documentAfterUpdate);

        // Close the OJAI connection
        connection.Close();
    }
}
