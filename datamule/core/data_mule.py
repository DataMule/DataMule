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
            self.connection_string = connector['connector']['connection_string']
            self.schema = connector['connector']['schema']
            self.table_name = connector['connector']['table_name']
            self.delta_type = connector['connector']['delta']['type']
            self.delta_value = connector['connector']['delta']['value']
            self._upload_to_db()
            self._insert_data_process()



    def _get_schema(self):
        if (self.schema == 'auto'):
            parser = Parser(self.format)
            if self.format == 'csv':
                return parser.create_schema(self.connector)
            elif self.format == 'json':
                return parser.create_schema(self.connector)

    def _get_db(self):
        data_mule_docker = DataMuleDocker(self.db_type)
        dict_user_password = data_mule_docker.run()
        self.user_name = dict_user_password['user_name']
        self.password = dict_user_password['password']

    def _upload_to_db(self):
        uploader = Uploader(self.db_type, self.user_name, self.password)
        if self.protocol == 'http':
            uploader.upload_http(self.connection_string)

    def _insert_data_process(self):
        data_process = DataProcess()
        data_process.insert_process(name=self.table_name, local_or_container='container',
                                    delta=self.delta_value, table_name=self.table_name, datasource_type=self.db_type)


