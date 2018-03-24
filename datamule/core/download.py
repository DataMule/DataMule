import pandas as pd
import requests


class Downloader():

    def download_http(self, http_link):
        chunksize = 1000000
        for chunk in pd.read_csv(http_link, chunksize=chunksize):
            self._process(chunk)


    def _process(self, df_write):
        pass
