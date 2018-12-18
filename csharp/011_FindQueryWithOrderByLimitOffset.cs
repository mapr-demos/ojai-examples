using System;
using MapRDB.Driver;
using MapRDB.Driver.Ojai;

public class FindQueryWithOrderByLimitOffset
{
	public async void FindQueryWithOrderByLimitOffset()
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

        // Create an OJAI query
        var query = connection
            .NewQuery()
                .Select("_id", "firstName", "lastName", "address.zipCode")
                .Offset(2)
                .Limit(1)
                .OrderBy("_id", SortOrder.ASC)
            .Build();

        // Fetch OJAI Documents by query
        var queryResult = store.Find(query);

        var documentStream = await queryResult.GetDocumentAsyncStream().GetAllDocuments();
        // Print OJAI Documents from document stream
        foreach (var document in documentStream)
        {
            Console.WriteLine(document.ToJsonString());
        }

        // Close the OJAI connection
        connection.Close();
    }
}
