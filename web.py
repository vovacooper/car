from functools import wraps

from flask import request, Response, Flask, make_response ,json
from flask import render_template
from classes.logger import logger


#from flask.ext.uwsgi_websocket import GeventWebSocket
from flask.ext.uwsgi_websocket import WebSocket
#from flask_uwsgi_websocket.websocket import WebSocket



########################################################################################################################
from modules.data_module import data_module


app = Flask(__name__)
#app.debug = True
#app.config['DEBUG'] = True

'''
this is for loadimg flask admin like a blueprint
'''
#Admin
from flask.ext.admin import Admin
admin = Admin(app)
#add admin
import modules.admin_module

'''
WEBSOCKET
'''
ws = WebSocket(app)
#ws = GeventWebSocket(app)




########################################################################################################################
app.register_blueprint(data_module)


########################################################################################################################
@app.route("/")
def hello():
    return render_template('under_construction.html')


#example
@app.route('/hello/')
@app.route('/hello/<name>')
def hello1(name=None):
    return render_template('name_template.html', name=name)

########################################################################################################################
#HEADERS
def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator


def appId(f):
    """This decorator passes X-Robots-Tag: noindex"""
    @wraps(f)
    @add_response_headers({'X-IBS-APP_ID': 'akldqwdj283742j9834h2d'})
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

@app.route('/h')
@add_response_headers({'X-IBS-APP_ID': 'akldqwdj283742j9834h2d'})
def not_indexed():
    """
    This page will be served with X-Robots-Tag: noindex
    in the response headers
    """
    return "Check my headers!"

@app.route('/headers')
def headers():
    api_id = request.headers.get('X-IBS-API-ID')
    app_id = request.headers.get('X-IBS-APP-ID')
    response_data = \
        {
            "vova": "cooper",
            "api_id": api_id,
            "app_id": app_id,
        }
    response_json = json.dumps(response_data)

    return Response(response=response_json,
                        status=200,
                        mimetype="application/json",
                        headers={"api_id": api_id, "app_id": app_id})

########################################################################################################################
#WEBSOCKET
########################################################################################################################
@app.route("/ws")
def web_socket():
    return render_template('websocket_test.html')


@ws.route('/websocket')
def web_socket_echo(ws):
    try:
        logger.warning("/websocket")
        while True:
            msg = ws.receive()
            if msg is not None:
                ws.send(msg)
            else:
                return
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response

@ws.route('/echo')
def echo(ws):
    while True:
        message = ws.receive()
        ws.send(message)


########################################################################################################################
if __name__ == "__main__":
    logger.info("Starting application!")
    app.run(host='0.0.0.0')
    #, gevent=1000
