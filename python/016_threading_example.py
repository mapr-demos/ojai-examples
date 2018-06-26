"""Following example works with Python Client"""
import threading
import time

from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

"""Create a connection, get store, insert_or_replace/update document in
 store via thread using same connection"""

# Create a connection string using path:user@password
connection_str = "localhost:5678?auth=basic;user=mapr;password=mapr;" \
          "ssl=true;" \
          "sslCA=/opt/mapr/conf/ssl_truststore.pem;" \
          "sslTargetNameOverride=node1.mapr.com"

# Create connection from connection_url
# Can share connection for processes,
# so need to only one connection instance for all threads
connection = ConnectionFactory.get_connection(connection_str)


# Create child for sample threading implementation
class MyThread(threading.Thread):
    # Implement __init__() method, which takes thread name and
    # connection object
    def __init__(self, name, connection):
        threading.Thread.__init__(self)
        self.name = name
        self.connection = connection

    # Implement run() method
    def run(self):
        # Print that thread started with threadName
        print('\n Start thread ', self.name)

        # Get a store and assign it as a DocumentStore object
        store = connection.get_or_create_store('/tmp/store_name')

        # Insert 15 documents, represented as Python dictionaries,
        # into DocumentStore
        for index in range(15):
            store.insert_or_replace(doc={'_id': str(index), 'name': 'Greg'})

        # Create DocumentMutation object using the OJAIConnection object
        mutation = connection.new_mutation()

        # Set mutation value
        mutation.set_or_replace(field_path='name', value='T')

        # Update 15 Document in store
        for index in range(15):
            store.update(_id=str(index), mutation=mutation)

        # Print that thread done with threadName
        print('\n Done thread ', self.name)


# This thread implementation return thread object
# so thread status can be checked via native methods
# Simple thread waiter for thread list:
def waiter(threads):
    for my_thread in threads:
        # Check that current thread is alive
        if my_thread.is_alive():
            time.sleep(1)
            # Wait until current thread finished
            waiter(threads)
        # Move to the next thread if this is not alive
        elif not my_thread.is_alive():
            pass


# Create list instance for storing created threads objects
thread_list = []

# Create and run 10 threads
for i in range(10):
    # Create thread instance using MyThread and OJAIConnection object
    thread = MyThread(name='Thread-{0}'.format(str(i)),
                      connection=connection)

    # Start current thread
    thread.start()

    # Append thread object into thread_list
    thread_list.append(thread)

# Wait until all threads will finished
waiter(thread_list)

# Close connection
connection.close()
