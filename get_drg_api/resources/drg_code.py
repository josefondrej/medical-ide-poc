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
    data = DRGCode.parser.parse_args()
    code, distance = text_to_code(data["text"])

    return {"code": code, "distance": distance}, 200
