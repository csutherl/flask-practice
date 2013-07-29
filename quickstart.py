from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

from db_connector import row

@app.route('/get')
def hello_world():
    return str(row);

if __name__ == '__main__':
    app.run()
