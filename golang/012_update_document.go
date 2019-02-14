package main

import (
	"fmt"
	client "github.com/mapr/maprdb-go-client"
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
	documentId := "user0002"

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
	fmt.Printf("Document with id %v before update.\n %v", documentId, documentBeforeUpdate.AsJsonString())

	// Create mutation to update the zipCode field
	mutation := map[string]interface{}{"$set": map[string]interface{}{"address.zipCode": 95196}}

	// Execute update
	err = store.Update(client.BosiFromString(documentId), client.MosmFromMap(mutation))
	if err != nil {
		panic(err)
	}

	// Print the document after update
	documentAfterUpdate, err := store.FindByIdString(documentId)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Document with id %v after update.\n %v", documentId, documentAfterUpdate.AsJsonString())

	// Close connection
	connection.Close()
}
