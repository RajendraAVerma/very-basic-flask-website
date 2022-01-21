from flask import Flask


app = Flask(__name__)


@app.route('/home/<string:name>')
def hello(name):
    return f"<b>hello world</b> {name}"


if __name__ == "__main__":
    app.run(debug=True)
