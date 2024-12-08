from flask import Flask
from flask import render_template as rt
from flask import url_for

test7 = Flask(__name__)

@test7.route('/')
def index():
    return rt('index.html')

@test7.route('/home')
def home():
    return rt('home.html')

@test7.route('/user/<string:name>/<string:id>')
def user1(name, id):
    return 'User page:' + ' ' + name + id

@test7.route('/about')
def about():
    return ')_12gbg'

if __name__ == '__main__':
    test7.run(debug = True)
