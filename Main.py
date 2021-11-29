import flask

app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('index.html')

app.run('127.0.0.1', '5900')