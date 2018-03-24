import pandas as pd
import requests
from sqlalchemy import create_engine


class Uploader():

    def __init__(self, db_type, user_name, password):
        self.db_type = db_type
        self.user_name = user_name
        self.password = password

    def upload_http(self, http_link):
        chunksize = 1000000
        for chunk in pd.read_csv(http_link, chunksize=chunksize):
            self._write_to_db(chunk)


    def _write_to_db(self, df_write, db_table):
        if (self.db_type == 'postgres'):
            engine = create_engine('postgresql://{}:{}@localhost:5432/postgres'.format(self.user_name, self.password))
            df_write.to_sql(db_table, con=engine)
        else:
            raise Exception("Database type {} not found".format(self.db_type))

    def load_rest(self, connection_params, db_table):
        # TODO: Add looping to get more than on set of results
        r = requests.get(**connection_params)
        if r.status_code == 200:
            df = pd.read_json(r.content)
            self._write_to_db(df, db_table)
        else:
            raise Exception(r.content)
