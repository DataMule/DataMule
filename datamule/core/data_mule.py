from datamule.core.parser import Parser
from datamule.core.upload import Uploader
from datamule.core.data_process import DataProcess
from datamule.docker.container import DataMuleDocker


class DataMule():

    def __init__(self, protocol, connectors, auth, format_type, db_type, api_token=None):
        self.protocol = protocol
        self.connectors = connectors
        self.auth = auth
        self.format_type = format_type
        self.db_type = db_type
        self.api_token = api_token

    def run(self):
        self._get_db()
        for connector in self.connectors:
            connection_string = connector['connector']['connection_string']
            schema = connector['connector']['schema']
            table_name = connector['connector']['table_name']
            delta_type = connector['connector']['delta']['type']
            delta_value = connector['connector']['delta']['value']
            self._upload_to_db(connection_string, table_name)
            self._insert_data_process(table_name, delta_value)



    def _get_schema(self):
        if (self.schema == 'auto'):
            for connector in self.connectors:
                parser = Parser(self.format_type)
                if self.format_type == 'csv':
                    return parser.create_schema(connector['connector']['connection_string'])
                elif self.format_type == 'json':
                    return parser.create_schema(connector['connector']['connection_string'])

    def _get_db(self):
        data_mule_docker = DataMuleDocker(self.db_type)
        dict_user_password = data_mule_docker.run()
        self.user_name = dict_user_password['username']
        self.password = dict_user_password['password']

    def _upload_to_db(self, connection_string, table_name):
        uploader = Uploader(self.db_type, self.user_name, self.password)
        # if self.protocol == 'http':
        uploader.upload_http(connection_string, table_name)

    def _insert_data_process(self, table_name, delta_value):
        data_process = DataProcess()
        data_process.insert_process(name=table_name, local_or_container='container',
                                    delta=delta_value, table_name=table_name, datasource_type=self.db_type)


