import itertools
import pandas as pd
import requests
import sys
from sqlalchemy import create_engine


class Uploader():

    def __init__(self, db_type, user_name, password):
        self.db_type = db_type
        self.user_name = user_name
        self.password = password

    def upload_http(self, http_link, table_name):
            df_http = pd.read_csv(http_link)
            print("processing file")
            self._write_to_db(df_http, table_name)

    def _write_to_db(self, df_write, table_name):
        if (self.db_type == 'postgres'):
            engine = create_engine('postgresql://{}:{}@localhost:5432/postgres'.format(self.user_name, self.password))
            df_write.to_sql(table_name, con=engine, if_exists='append')
        else:
            raise Exception("Database type {} not found".format(self.db_type))

    def load_rest(self, connection_string, headers, table_name):
        # TODO: Add looping to get more than on set of results
        for page in itertools.count():
            params = {'page': str(page+1)}
            r = requests.get(connection_string, headers=headers, params=params)
            if r.status_code == 200:
                df = pd.read_json(r.content)
                self._write_to_db(df, table_name)
            else:
                break

