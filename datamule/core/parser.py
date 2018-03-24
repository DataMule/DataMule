import pandas as pd


class Parser():

    def __init__(self, format):
        self.format = format

    def create_schema(self, file):
        if self.format == 'csv':
            data_set = pd.read_csv(file, nrows=1)
        elif self.format == 'json':
            data_set = pd.read_json(file, nrows=1)
        else:
            data_set = pd.read_csv(file, nrows=1)
        data_set_schema = pd.io.sql.get_schema(data_set, 'data')
        return data_set_schema
