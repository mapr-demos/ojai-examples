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

# options for find request
options = {
    'ojai.mapr.query.include-query-plan': True,
    'ojai.mapr.query.result-as-document': True,
    'ojai.mapr.query.timeout-milliseconds': 10000
}

# fetch all OJAI Documents from table
query_result = store.find(query, options=options)

# get query plan
print(query_result.get_query_plan())

doc_stream = query_result
# Print OJAI Documents from document stream
for doc in doc_stream:
    print(doc.as_dictionary())

# close the OJAI connection
connection.close()
