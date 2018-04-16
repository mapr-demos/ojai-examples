from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection = ConnectionFactory.get_connection(url='localhost:5678')

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

# fetch the OJAI Document by its '_id' field
doc = store.find_by_id("user0001")

# Print the OJAI Document
print(doc.as_dictionary())

# close the OJAI connection
connection.close()
