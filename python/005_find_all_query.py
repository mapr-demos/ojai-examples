from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection_str = "localhost:5678?auth=basic;user=mapr;password=mapr;" \
          "ssl=true;" \
          "sslCA=/opt/mapr/conf/ssl_truststore.pem;" \
          "sslTargetNameOverride=node1.mapr.com"
connection = ConnectionFactory.get_connection(connection_str=connection_str)

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

# Build an OJAI query
query = connection.new_query().build()

# fetch all OJAI Documents from table
query_result = store.find(query,
                          include_query_plan=True,
                          results_as_document=True)

# get query plan
print(query_result.get_query_plan())

doc_stream = query_result
# Print OJAI Documents from document stream
for doc in doc_stream:
    print(doc.as_dictionary())

# close the OJAI connection
connection.close()
