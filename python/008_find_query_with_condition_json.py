from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection = ConnectionFactory.get_connection(url='localhost:5678')

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

# Build an OJAI query
query = connection.new_query().where("{\"$eq\": {\"address.zipCode\": 95196}}").build()

# fetch OJAI Documents by query
query_result = store.find(query)

# Print OJAI Documents from document stream
for doc in query_result.iterator():
    print(doc.as_dictionary())

# close the OJAI connection
connection.close()
