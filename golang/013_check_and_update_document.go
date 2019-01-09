package main

import (
	"fmt"
	client "github.com/mapr/private-maprdb-go-client"
)

func main() {
	// Create connection string
	connectionString := "192.168.33.11:5678?" +
		"auth=basic;" +
		"user=mapr;" +
		"password=mapr;" +
		"ssl=true;" +
		"sslCA=/opt/mapr/conf/ssl_truststore.pem;" +
		"sslTargetNameOverride=node1.cluster.com"

	storeName := "/demo_table"
	documentId := "user0001"

	// Create a connection to DAG
	connection, err := client.MakeConnection(connectionString)
	if err != nil {
		panic(err)
	}

	// Get a store and assign it as a DocumentStore struct
	store, err := connection.GetStore(storeName)
	if err != nil {
		panic(err)
	}

	// Print the document before update
	documentBeforeUpdate, err := store.FindByIdString(documentId)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Document with id %v before update.\n %v\n", documentId, documentBeforeUpdate.AsJsonString())

	// Create mutation to update the zipCode field
	mutation := map[string]interface{}{"$put": map[string]interface{}{"address.zipCode": 99999}}

	// Create condition
	condition := map[string]interface{}{"$eq": map[string]interface{}{"address.street": "320 Blossom Hill Road"}}

	// Execute update
	// Returns True if condition True and document was updated.
	res, err := store.CheckAndUpdate(
		client.BosiFromString(documentId),
		client.MoscFromMap(condition),
		client.MosmFromMap(mutation))
	if err != nil {
		panic(err)
	}

	// Print the document after update
	documentAfterUpdate, err := store.FindByIdString(documentId)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Update result: %v.\nDocument with id %v after update.\n %v\n",
		res,
		documentId,
		documentAfterUpdate.AsJsonString())

	// Close connection
	connection.Close()
}
