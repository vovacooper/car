from flask import Flask
from flask import url_for, redirect
from flask import render_template
from flask.ext.uwsgi_websocket import GeventWebSocket

#from classes import logger

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
@app.route("/ws")
def web_socket():
    return render_template('websocket_test.html')


@ws.route('/websocket')
def web_socket_echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else:
            return

@gws.route('/echo')
def echo(ws):
    while True:
        message = ws.receive()
        ws.send(message)


########################################################################################################################
if __name__ == "__main__":
    app.run()


