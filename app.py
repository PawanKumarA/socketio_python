from flask import Flask, request, session
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import json
import numpy as np
import pandas as pd
from flask import Flask, request, session


Event_Connect_status = 'Connect_Status'
Event_Connect = 'connect'
Event_Disonnect_status = 'Disconnect'
Event_Disconnect = 'disconnect'

app = Flask(__name__)



cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, path='/socket', cors_allowed_origins="*" ,manage_session=True, async_handlers=False, ping_timout=120000, ping_interval=2000 )


@app.route('/test', methods=['GET'])
def test():
    return "Welcome to REST "


@socketio.on(Event_Connect)
def connect():
    session[request.sid] = {}
    print("session id ->", request.sid)
    emit(Event_Connect_status, "hello good morning")

    print("client connected : ip addr : " + request.remote_addr)


@socketio.on(Event_Disconnect)
def disconnect():
    print(session)
    emit(Event_Disonnect_status, "Good Bye")


if __name__ == '__main__':
    print("server up and running....")
    socketio.run(app, host='0.0.0.0', port= 5000,debug=True,  use_reloader=False )

