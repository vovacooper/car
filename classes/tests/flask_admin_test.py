
from flask import Flask
from flask.ext.admin import Admin


app = Flask(__name__)


admin = Admin(app)

if __name__ == '__main__':

    # Start app
    app.run()