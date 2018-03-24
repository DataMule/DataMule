import pandas as pd
import requests


class Uploader():

    def uploader_http(self, http_link):
        chunksize = 1000000
        for chunk in pd.read_csv(http_link, chunksize=chunksize):
            self._write_to_db(chunk)


    def _write_to_db(self, df_write, db_table):
        df_write.to_sql(db_table)
