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

	// Create a connection to data access server
	connection, err := client.MakeConnection(connectionString)
	if err != nil {
		panic(err)
	}

	// Json string or map from which the Document will be created
	newMap := map[string]interface{}{
		"_id":  "id001",
		"name": "Joe",
		"age":  50,
		"address": map[string]interface{}{
			"street": "555 Moon Way",
			"city":   "Gotham",
		},
	}

	// Create new document from json_document
	newDocument := connection.CreateDocumentFromMap(newMap)

	// Print the new OJAI Document
	fmt.Println(newDocument.AsJsonString())

	// Close connection
	connection.Close()
}
