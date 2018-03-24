import datamule.core.upload
import os

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
uploader = datamule.core.upload.Uploader("postgres")

params = {"url": "https://sandbox.api.it.nyu.edu/course-catalog-exp/courses",
          "headers": {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}}

(uploader.load_rest(params, "courses"))
