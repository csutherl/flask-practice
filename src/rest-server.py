from flask import Flask, abort, make_response, jsonify
# from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
# from flask.ext.httpauth import HTTPBasicAuth
import json

app = Flask(__name__, static_url_path = "")
api = Api(app)
app.config.from_pyfile('../conf/config.py')

# auth = HTTPBasicAuth()
 
# @auth.get_password
# def get_password(username):
#     if username == 'miguel':
#         return 'python'
#     return None
 
# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify( { 'message': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
    
default_records = [
    {
        'id': 0,
        'value': 0
    }
]
 
default_record_fields = {
    'id': fields.Integer,
    'value': fields.Integer
}

class RecordListAPI(Resource):
    # decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='No record ID provided', location='json')

        from db_connector import DB_Connector
        self.connector = DB_Connector()

        super(RecordListAPI, self).__init__()
        
    def get(self):
        # return {'records': map(lambda t: marshal(t, default_record_fields), default_records)}
        return json.loads(self.connector.getAll())

class RecordAPI(Resource):
    # decorators = [auth.login_required]
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')

        super(RecordAPI, self).__init__()

    def get(self, id):
        rec = filter(lambda t: t['id'] == id, default_records)

        if len(rec) == 0:
            abort(404)

        return {'record': marshal(rec[0], default_record_fields)}

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})

    """ Adding this header so that chrome will let me test locally """
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

api.add_resource(RecordListAPI, '/rest/records', endpoint='records')
api.add_resource(RecordAPI, '/rest/record/<int:id>', endpoint='record')

if __name__ == '__main__':
    app.run(debug=True)
