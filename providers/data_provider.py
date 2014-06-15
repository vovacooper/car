__author__ = 'vovacooper'

#from classes.mongo import db
#from providers.geo_ip_provider import GeoIpProvider
#from classes.logger import logger


########################################################################################################################
class DataProvider():
    _request_data = {}

    def __init__(self, request_data):
        self._request_data = request_data
        self._result = \
            {
                "di": {"category": "", "domain": "", "type": "", "country_code": "", "r_domain": ""},
                "mt": {"url": "", "width": 0, "height": 0},
                "sl": {"l_url": "", "r_url": "", "b_url": ""}
            }

    def get_data(self):
        return \
            {
                "name": "vovacooper",
                "category": "haha",
                "type": "data from data_provider",
                "tags": self._request_data["tags"]
            }
