from flask import Flask
from flask_restful import Api
from .resource import *
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(History,"/history")

if __name__ == "__main__":
    app.run(debug=True)

    # http://127.0.0.1:5000/