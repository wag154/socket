from applications import app,db,socketio
from applications.model import Test_class
from flask import jsonify , request
from flask_socketio import emit 
import json

@app.route("/enter")
def index():
    resp = Test_class.query.all()
    data = [d.__dict__ for d in resp]
    for item in data:
        item.pop('_sa_instance_state',None)
    return jsonify(data), 200

@app.route("/add", methods = ["POST","GET"])
def add():
    data = request.data
    json_data = json.loads(data)
    try:
        if "name" not in json_data and "message" not in json_data:
         return "fail"
        else :
            entry = Test_class(name = json_data["name"], message = json_data["message"])
            db.session.add(entry)
            db.session.commit()
            return "PASSED!"
    except:
        return "Wrong key name for sent information, (only accepts 'name' and 'message')"
#prints to console connected
@socketio.on('connect')
def handle_connect():
    print("Connected user")
#the socket.on('value') can be thought of as "event" that we can define endpoints for and the frontend can use. 
@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

#on refers to the frontend way to emit the information
@socketio.on('message')
def handle_message(data):
    #data is information received
    print('Received message',data)
    emit('message', data,broadcast=True)
    