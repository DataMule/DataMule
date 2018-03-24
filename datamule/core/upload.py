import pandas as pd
import requests
from sqlalchemy import create_engine


class Uploader():

    def __init__(self, db_type):
        self.db_type = db_type

    def upload_http(self, http_link):
        chunksize = 1000000
        for chunk in pd.read_csv(http_link, chunksize=chunksize):
            self._write_to_db(chunk)


    def _write_to_db(self, df_write, db_table):
        if (self.db_type == 'postgres'):
            engine = create_engine('postgresql://{}:{}@localhost:5432/postgres'.format(self.user_name, self.password))
            df_write.to_sql(db_table, con=engine)
