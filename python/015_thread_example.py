"""Following example works with Python Client"""
import thread
import time
from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

"""Create a connection, get store, insert_or_replace/update document in
 store via thread using same connection"""


# Create method which will be used for threads
def run_thread(name, conn):
    # Print that thread started with threadName
    print('\n Start thread ', name)

    # Get a store and assign it as a DocumentStore object
    store = conn.get_or_create_store('/tmp/store_name')

    # Insert 15 documents, represented as Python dictionaries,
    # into DocumentStore
    for index in range(15):
        store.insert_or_replace(doc={'_id': str(index), 'name': 'Greg'})

    # Create DocumentMutation object using the OJAIConnection object
    mutation = conn.new_mutation()

    # Set mutation value
    mutation.set_or_replace(field_path='name', value='T')

    # Update 15 Document in store
    for index in range(15):
        store.update(_id=str(index), mutation=mutation)

    # Print that thread done with threadName
    print('\n Done thread ', name)


# Create a connection string using path:user@password
connection_str = "localhost:5678?auth=basic;user=mapr;password=mapr;" \
          "ssl=true;" \
          "sslCA=/opt/mapr/conf/ssl_truststore.pem;" \
          "sslTargetNameOverride=node1.mapr.com"

# Create connection from connection_url
# Can share connection for processes,
# so need to only one connection instance for all threads
connection = ConnectionFactory.get_connection(connection_str)

# Create 10 threads using the same connection instance
for i in range(10):
    thread_name = 'Thread-{}'.format(str(i))
    thread.start_new_thread(run_thread, (thread_name, connection,))

# This thread implementation doesn't return thread object
# so thread status cannot be checked
# Wait 10 seconds
time.sleep(10)

# Close connection
connection.close()
