from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection = ConnectionFactory.get_connection(url="localhost:5678")

# Get a store and assign it as a DocumentStore object
store = connection.get_store("/sample_store1")

for i in range(1, 10):
    json_dict = {"_id": "id00" + str(i),
                 "name": "Joe" + str(i),
                 "age": i,
                 "address": {
                     "street": str(i) + " Moon Way",
                     "city": "Gotham"}
                 }

    # Create new document from json_document
    new_document = connection.new_document(dictionary=json_dict)
    # Print the OJAI Document
    print(new_document.as_json_str())

    # Insert the OJAI Document into the DocumentStore
    store.insert_or_replace(new_document)

# close
connection.close()

