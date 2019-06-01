from flask import Flask

pyladiesdo = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    pyladiesdo.run()