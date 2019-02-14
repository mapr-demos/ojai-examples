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

	// Fetch all OJAI Documents from table
	findResult, err := store.FindAll(&client.FindOptions{IncludeQueryPlan: false, ResultAsDocument: true})

	// Print OJAI Documents from document stream
	for _, doc := range findResult.DocumentList() {
		fmt.Println(doc)
	}

	// Close connection
	connection.Close()
}
