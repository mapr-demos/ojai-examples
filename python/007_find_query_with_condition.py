from mapr.ojai.ojai_query.QueryOp import QueryOp
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
query = connection.new_query().where(connection.new_condition().is_('address.zipCode', QueryOp.EQUAL, 95196)
                                     .close().build()).build()

# fetch the OJAI Documents by query
query_result = store.find(query)

# Print OJAI Documents from document stream
for doc in query_result:
    print(doc)

# close the OJAI connection
connection.close()
