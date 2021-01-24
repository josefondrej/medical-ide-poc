from flask import Flask, render_template
from flask_restful import Api

from get_drg_api.resources.drg_code import DRGCode

app = Flask(__name__)
api = Api(app)

api.add_resource(DRGCode, '/text/')


@app.route("/")
def main():
  return render_template("index.html")


if __name__ == '__main__':
  app.run(port=5001, debug=True)
