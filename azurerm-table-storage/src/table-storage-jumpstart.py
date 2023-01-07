from azure.data.tables import TableServiceClient, TableClient


class TableStorageOperations:

    def __init__(self):
        connection_string = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=teststorageacct99;AccountKey=<your-access-key-here>;BlobEndpoint=https://teststorageacct99.blob.core.windows.net/;FileEndpoint=https://teststorageacct99.file.core.windows.net/;QueueEndpoint=https://teststorageacct99.queue.core.windows.net/;TableEndpoint=https://teststorageacct99.table.core.windows.net/"
        self.table_service_client = TableServiceClient.from_connection_string(conn_str=connection_string)
        # self.table_client = self.table_service_client.get_table_client(table_name="employeetable99")
        self.table_client = TableClient.from_connection_string(conn_str=connection_string, table_name="employeetable99")

    def create_entity(self):
        EMPLOYEE_ID = u'001234'
        EMPLOYEE_NAME = u'Arun Boppudi'

        my_entity = {
            u'PartitionKey': EMPLOYEE_NAME,
            u'RowKey': EMPLOYEE_ID,
            u'Salary': 4500000,
            u'Age': 36,
            u'Comments': u"An architect with extreme learning capabilities"
        }
        entity = self.table_client.create_entity(entity=my_entity)

    def query_table(self):
        my_filter = "PartitionKey eq 'RedMarker'"
        entities = self.table_client.query_entities(query_filter=my_filter)
        for entity in entities:
            for key in entity.keys():
                print(entity[key])


ops = TableStorageOperations()
# ops.create_entity()
ops.query_table()
