from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection = ConnectionFactory.get_connection(url='localhost:5678')

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

# Build an OJAI query
query = connection.new_query().build()

# fetch all OJAI Documents from table
query_result = store.find(query, include_query_plan=True)

# get query plan
print(query_result.get_query_plan())

doc_stream = query_result.iterator()
# Print OJAI Documents from document stream
for doc in doc_stream:
    print(doc.as_dictionary())

# close the OJAI connection
connection.close()
