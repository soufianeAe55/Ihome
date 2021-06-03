from flask import Flask

app = Flask(__name__)

app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return "Hello world !"
