"""
Resource for Texts

"""
from flask import jsonify, request
from flask.ext.restful import Resource

from texter import send_message


class TextResource(Resource):
    """
    Api Resource for texts

    """
    def post(self):
        try:
            send_message(**request.get_json())
        except ValueError as ex:
            response = jsonify({'message': ex.message})
            response.status_code = 400
            return response
