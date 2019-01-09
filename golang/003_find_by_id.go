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

	// Fetch the OJAI Document by its '_id' field
	doc, err := store.FindByIdString("id0001")
	if err != nil {
		panic(err)
	}

	// Print the OJAI Document
	fmt.Println(doc.AsJsonString())

	// Close connection
	connection.Close()
}
