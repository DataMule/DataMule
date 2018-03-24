import pandas as pd


class Parser():

    def __init__(self, type_file):
        self.type_file = type_file

    def create_schema_csv(self, file):
        data_set = pd.read_csv(file, nrows=1)
        data_set_schema = pd.io.sql.get_schema(data_set, 'data')
        return data_set_schema

    def parse_csv(self, file):
        first = pd.read_csv(file, nrows=2)
