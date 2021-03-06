from flask import jsonify
from flask_restful import Resource

# Example code, does nothing atm
class getBackgroundColor(Resource):
    def get(self):
        return jsonify({"bg_color": "#2AABF9"}) 

