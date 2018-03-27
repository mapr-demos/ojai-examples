from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection = ConnectionFactory.get_connection(url="localhost:5678")

# Get a store and assign it as a DocumentStore object
store = connection.get_store("/sample_store1")

# fetch the OJAI Document by its '_id' field
doc_stream = store.find()

# Print OJAI Documents from document stream
for doc in doc_stream:
    print(doc.as_json_str())

# close
connection.close()
