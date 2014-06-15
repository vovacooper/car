__author__ = 'vovacooper'


from providers.data_provider import DataProvider

from flask import Blueprint, request, Response, json

from classes.logger import logger

########################################################################################################################
data_module = Blueprint("data_module", __name__, url_prefix="/data")


########################################################################################################################
@data_module.route("/init")
def get_data():
    try:
        request_data = \
            {
                "ip": request.remote_addr,
                "callback": request.args.get("callback", False),
                "tags": request.args.get("tags", False)
            }

        #init data provider
        data_provider = DataProvider(request_data)
        #get data from provider
        response_data = data_provider.get_data()
        #make json
        response_json = json.dumps(response_data)

        if request_data["callback"]:
            response_json = "{0}({1})".format(request_data["callback"], json.dumps(response_data))

        return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response


