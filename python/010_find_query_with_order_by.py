from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection_str = "localhost:5678?auth=basic;user=mapr;password=mapr;" \
          "ssl=true;" \
          "sslCA=/opt/mapr/conf/ssl_truststore.pem;" \
          "sslTargetNameOverride=node1.mapr.com"
connection = ConnectionFactory.get_connection(connection_str=connection_str)

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

# Create an OJAI query
query = {"$select": ["_id", "firstName"], "$orderby": {"_id": "asc"}}

# fetch OJAI Documents by query
query_result = store.find(query)

# Print OJAI Documents from document stream
for doc in query_result:
    print(doc)

# close the OJAI connection
connection.close()
