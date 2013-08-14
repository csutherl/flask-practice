import json

from flask import Flask, abort, make_response
from flask.ext.restful import Api, Resource, reqparse
from src.server.sqlalchemy_connector import DB_Connector


app = Flask(__name__, static_url_path = "", static_folder="../client")

# standard flask stuff
@app.route('/')
def index():
    return app.send_static_file("index.html")

api = Api(app)
app.config.from_pyfile('../../conf/config.py')

class RecordListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('id', type=int, required=True, help='No record ID provided', location='json')

        self.connector = DB_Connector()

        super(RecordListAPI, self).__init__()
        
    def get(self):
        return json.loads(self.connector.getAll())

class RecordAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('id', type=int, location='json')

        self.connector = DB_Connector()

        super(RecordAPI, self).__init__()

    def get(self, name):
        rec = json.loads(self.connector.getOne(name))

        if len(rec) == 0:
            abort(404)

        return rec

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})

    """ Adding this header so that chrome will let me test locally """
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

api.add_resource(RecordListAPI, '/rest/records', endpoint='records')
api.add_resource(RecordAPI, '/rest/record/<string:name>', endpoint='record')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
