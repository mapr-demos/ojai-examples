"""Following example works with Python Client"""

import multiprocessing
from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

"""Create a connection, get store, insert_or_replace/update document in
 store via multiprocessing"""

# Create a connection string using path:user@password
connection_str = "localhost:5678?auth=basic;user=mapr;password=mapr;" \
          "ssl=true;" \
          "sslCA=/opt/mapr/conf/ssl_truststore.pem;" \
          "sslTargetNameOverride=node1.mapr.com"


# Create method which will be used for multiprocessing
def sample():
    # Create connection from connection_url
    # Cannot share connection for processes,
    # so need to create connection for each process.
    connection = ConnectionFactory().get_connection(connection_str=connection_str)

    # Get a store and assign it as a DocumentStore object
    store = connection.get_or_create_store('/tmp/store_name')

    # Insert 15 documents, represented as Python dictionaries,
    # into DocumentStore
    for i in range(15):
        store.insert_or_replace(doc={'_id': str(i), 'name': 'Greg'})

    # Create DocumentMutation object using the OJAIConnection object
    mutation = connection.new_mutation()

    # Set mutation value
    mutation.set_or_replace(field_path='name', value='T')

    # Update 15 Document in store
    for i in range(15):
        store.update(_id=str(i), mutation=mutation)


# Create simple method for run process from Pool
def run(unused_var):
    pass


# Create data for multiprocessing
proces_count = 7
map_iterable = [1]  # simple iterator

# Create Pool object using the function and process_count value
p = multiprocessing.Pool(proces_count, initializer=sample)

# Run processes from the Pool
p.map(run, map_iterable)
