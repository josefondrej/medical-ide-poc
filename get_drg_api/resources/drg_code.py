import json

from flask import request
from flask_restful import reqparse, Resource

from get_drg_api.text_to_code import text_to_code


class DRGCode(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('text',
                      type=str,
                      required=True,
                      help="This field cannot be left blank!"
                      )

  def post(self):
    raw_text = str(request.data, "utf-8")
    text = json.loads(raw_text)["text"]
    code, distance = text_to_code(text)
    result = {"code": code, "distance": distance}, 200
    return result
