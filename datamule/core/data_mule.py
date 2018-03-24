from datamule.core.parser import Parser
from datamule.core.upload import Uploader

class DataMule():

    def __init__(self, protocol, connector, auth, schema, delta, format, db_type):
        self.protocol = protocol
        self.connector = connector
        self.auth = auth
        self.schema = schema
        self.delta = delta
        self.format = format
        self.db_type = db_type

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
        uploader = Uploader(self.db_type)
        if self.protocol == 'http':
            uploader.upload_http(self.connector)

