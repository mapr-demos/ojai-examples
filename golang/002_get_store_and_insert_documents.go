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
	isExists, err := connection.IsStoreExists(storeName)
	if err != nil {
		panic(err)
	}
	var store *client.DocumentStore
	if isExists {
		store, err = connection.GetStore(storeName)
		if err != nil {
			panic(err)
		}
	} else {
		store, err = connection.CreateStore(storeName)
		if err != nil {
			panic(err)
		}
	}

	// Slice of maps from which the Document will be created
	documentArray := []map[string]interface{}{
		{
			"_id":       "user0000",
			"age":       35,
			"firstName": "John",
			"lastName":  "Doe",
			"address": map[string]interface{}{
				"street":  "350 Hoger Way",
				"city":    "San Jose",
				"state":   "CA",
				"zipCode": 95134,
			},
			"phoneNumbers": []interface{}{
				map[string]interface{}{"areaCode": 555, "number": 5555555},
				map[string]interface{}{"areaCode": "555", "number": "555-5556"},
			},
		},
		{
			"_id":       "user0001",
			"age":       26,
			"firstName": "Jane",
			"lastName":  "Dupont",
			"address": map[string]interface{}{
				"street":  "320 Blossom Hill Road",
				"city":    "San Jose",
				"state":   "CA",
				"zipCode": 95196,
			},
			"phoneNumbers": []interface{}{
				map[string]interface{}{"areaCode": 555, "number": 5553827},
				map[string]interface{}{"areaCode": "555", "number": "555-6289"},
			},
		},
		{
			"_id":       "user0002",
			"age":       45,
			"firstName": "Simon",
			"lastName":  "Davis",
			"address": map[string]interface{}{
				"street":  "38 De Mattei Court",
				"city":    "San Jose",
				"state":   "CA",
				"zipCode": 95142,
			},
			"phoneNumbers": []interface{}{
				map[string]interface{}{"areaCode": 555, "number": 5425639},
				map[string]interface{}{"areaCode": "555", "number": "542-5656"},
			},
		},
	}

	for _, docMap := range documentArray {
		// Create new document from json_document
		newDocument := connection.CreateDocumentFromMap(docMap)
		// Print the new OJAI Document
		fmt.Println(newDocument.AsJsonString())
		//Insert the OJAI Document into the DocumentStore
		store.InsertOrReplaceDocument(newDocument)
	}

	// Close connection
	connection.Close()
}
