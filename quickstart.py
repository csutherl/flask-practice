from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

import html

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return html.print_html(html)

if __name__ == '__main__':
    app.run()
