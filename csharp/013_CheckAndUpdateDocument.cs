using System;
using MapRDB.Driver;
using MapRDB.Driver.Ojai;

public class CheckAndUpdateDocument
{
	public void CheckAndUpdateDocument()
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

        var docId = "user0001";

        // Print the document before update
        var documentBeforeUpdate = store.FindById(docId);
        Console.WriteLine($"Document with id {docId} before update:");
        Console.WriteLine(documentBeforeUpdate);

        // Create mutation to update the zipCode field
        var mutation = connection.NewDocumentMutation().SetOrReplace("address.zipCode", 99999);

        // Create condition
        var condition = connection
            .NewQueryCondition()
                .Is("address.street", QueryOp.EQUAL, "320 Blossom Hill Road")
                .Close()
            .Build();

        // Execute CheckAndUpdate.
        // Returns True if condition True and document was updated
        var updateResult = store.CheckAndUpdate(docId, condition, mutation);

        Console.WriteLine(updateResult);

        // Print the document after update
        var documentAfterUpdate = store.FindById(docId);
        Console.WriteLine($"Document with id {docId} after update:");
        Console.WriteLine(documentAfterUpdate);

        // Close the OJAI connection
        connection.Close();
    }
}
