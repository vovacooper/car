from flask import Blueprint, request, Response, Flask, make_response ,json
from flask import url_for, redirect
from flask import render_template
from flask.ext.uwsgi_websocket import GeventWebSocket

from functools import wraps

from classes import logger

#from flask.ext.uwsgi_websocket import WebSocket
from flask_uwsgi_websocket.websocket import WebSocket

########################################################################################################################
from modules.data_module import data_module


app = Flask(__name__)
ws = WebSocket(app)
gws = GeventWebSocket(app)


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
@app.route("/ws")
def web_socket():
    return render_template('websocket_test.html')


@ws.route('/websocket')
def web_socket_echo(ws):
    try:
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

@gws.route('/echo')
def echo(ws):
    while True:
        message = ws.receive()
        ws.send(message)

from werkzeug.debug import DebuggedApplication

app.debug = True
if (app.debug ):
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
########################################################################################################################
if __name__ == "__main__":
    app.run(host='0.0.0.0')


