from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection_str = "localhost:5678?auth=basic;user=mapr;password=mapr;" \
                 "ssl=true;" \
                 "sslCA=/opt/mapr/conf/ssl_truststore.pem;" \
                 "sslTargetNameOverride=node1.mapr.com"
connection = ConnectionFactory.get_connection(connection_str=connection_str)

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

doc_id = 'user0001'

# Print the document before update
document_before_update = store.find_by_id(doc_id)
print("Document with id {0} before update".format(doc_id))
print(document_before_update)

# Create mutation to update the zipCode field
mutation = {'$put': {'address.zipCode': 99999}}

# Create condition
condition = {'$eq': {'address.street': '320 Blossom Hill Road'}}

# Execute check_and_update.
# Returns True if condition True and document was updated.
update_result = store.check_and_update(_id=doc_id,
                                       mutation=mutation,
                                       query_condition=condition)

print(update_result)

document_after_update = store.find_by_id(doc_id)
print('Document with id {0} after update'.format(doc_id))
print(document_after_update)
