from server import app, db


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
