#notes
'''

export FLASK_APP=flask_server.py set up the serve
flask run to start the server
export FLASK_DEBUG=1 to set up the code in debug mode so that any changes
will be affected live in the server

or just use app.run(debug=True)


'''


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hellow Home !"


@app.route("/about")
def about():
    return "<h1>About Page !"



if __name__ == '__main__':
    app.run(debug=True)


