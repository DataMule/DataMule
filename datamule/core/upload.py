import pandas as pd
import requests
from sqlalchemy import create_engine


class Uploader():

    def __init__(self, db_type, user_name, password):
        self.db_type = db_type
        self.user_name = user_name
        self.password = password

    def upload_http(self, http_link, table_name):
        chunksize = 1000000
        for chunk in pd.read_csv(http_link, chunksize=chunksize):
            print("processing file")
            self._write_to_db(chunk, table_name)


    def _write_to_db(self, df_write, db_table):
        # if (self.db_type == 'postgres'):
        engine = create_engine('postgresql://{}:{}@localhost:5432/postgres'.format(self.user_name, self.password))
        df_write.to_sql(db_table, con=engine, if_exists='append')
