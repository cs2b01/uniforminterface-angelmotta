from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola CS"
    #return render_template('index.html')

@app.route('/users')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Usuario)
    data = users[:]
    print("Read Users")
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_test_user', methods = ['GET'])
def create_test_users():
    db_session = db.getSession(engine)
    user = entities.Usuario(nombre="Piero", apellido="Morales", password="pieropass")
    db_session.add(user)
    db_session.commit()
    return "User created!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
