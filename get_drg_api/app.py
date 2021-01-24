from flask import Flask
from flask_restful import Api

from get_drg_api.resources.drg_code import DRGCode

app = Flask(__name__)
api = Api(app)

api.add_resource(DRGCode, '/text/')

if __name__ == '__main__':
  app.run(port=5000, debug=True)
