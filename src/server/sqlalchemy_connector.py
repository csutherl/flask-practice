import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, inspect
from src.server.settings import flask_config

class DB_Connector():

    def __init__(self):
        engine = create_engine('{}://{}:{}@{}:{}/{}'.format(
            flask_config['dbtype'],
            flask_config['user'],
            flask_config['pass'],
            flask_config['host'],
            flask_config['port'],
            flask_config['dbname']
        ))

        self.meta = MetaData()
        self.insp = inspect(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getTable(self, table_name):
        table = Table(table_name, self.meta)
        self.insp.reflecttable(table, None)

        return table

    def getAll(self):
        # Use all the SQL you like
        table = self.getTable('aw_jobexecution')
        res = self.session.query(table).all()
        json_res = self.to_json(res, table)

        return json_res

    def getOne(self, name):
        # Use all the SQL you like
        table = self.getTable('aw_jobexecution')
        res = self.session.query(table)\
            .filter(table.columns.name.like("%{}%".format(name))).all()
        json_res = self.to_json(res, table)

        return json_res

    def to_json(self, qry_results, table):
        """
            Jsonify the sql alchemy query result.
        """
        results = []
        if type(qry_results) is list:
            col_types = dict()
            for qry_result in qry_results:
                table_json = {}
                for col in table._columns:
                    v = getattr(qry_result, col.name)
                    if col.type in col_types.keys() and v is not None:
                        try:
                            table_json[col.name] = col_types[col.type](v)
                        except:
                            table_json[col.name] = "Error:  Failed to covert using ", str(col_types[col.type])
                    elif v is None:
                        table_json[col.name] = str()
                    else:
                        table_json[col.name] = v
                results.append(table_json)
            return json.dumps(results, cls=CustomEncoder)
        else:
            return self.to_json([qry_results], table)

# Who can't jsonify datetimes :P
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime):
            # is iso format ok, or do we want something different?
            return obj.isoformat()
        return json.JSONEncoder.default(self,obj)
