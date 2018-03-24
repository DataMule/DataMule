

class DataSet():

    def __init__(self, protocol, connector, auth, schema, delta):
        self.protocol = protocol
        self.connector = connector
        self.auth = auth
        self.schema = schema
        self.delta = delta