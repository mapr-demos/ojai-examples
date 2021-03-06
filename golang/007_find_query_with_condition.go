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

	// Options for find request
	options := &client.FindOptions{ResultAsDocument: true}

	// Create a condition
	condition, err := client.MakeCondition(client.Is("address.zipCode", client.EQUAL, 95196), client.Close())
	if err != nil {
		panic(err)
	}
	condition.Build()

	// Create an OJAI query
	query, err := client.MakeQuery(client.WhereCondition(condition))
	if err != nil {
		panic(err)
	}
	query.Build()

	// Fetch all OJAI Documents from table
	findResult, err := store.FindQuery(query, options)

	// Print OJAI Documents from document stream
	for _, doc := range findResult.DocumentList() {
		fmt.Println(doc)
	}

	// Close connection
	connection.Close()
}
