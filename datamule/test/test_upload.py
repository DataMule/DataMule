import datamule.core.upload
import datamule.core.data_mule
import os

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]

dm = datamule.core.data_mule.DataMule() # Busted
uploader = datamule.core.upload.Uploader("postgres", dm.user_name, dm.password)


params = {"url": "https://sandbox.api.it.nyu.edu/course-catalog-exp/courses",
          "headers": {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}}

(uploader.load_rest(params, "courses"))
