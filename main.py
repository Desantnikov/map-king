from flask import Flask, redirect, render_template, request
from flask_cors import cross_origin, CORS
from flask_socketio import SocketIO, join_room, emit, send
import json

import sys
from loguru import logger
from room import Room
from json_encoder import UniversalJsonEncoder
from config import MAP_SETTINGS, MAP_DEFAULTS, DIRECTIONS

app = Flask(__name__)




CORS(app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(app, cors_allowed_origins="*", log=logger)

rooms = []



@app.route('/')
@cross_origin()
def index():
    return "Please use /room/new"


@app.route('/room/new', methods=['GET'])
@cross_origin()
def create_room():
    #pre_configured = [len(rooms), logger]
    settings = [request.args.get(*parameter) for parameter in zip(MAP_SETTINGS, MAP_DEFAULTS)]
    parameters = settings + [len(rooms)] #pre_configured  # move to separate func

    rooms.append(Room(*parameters))  # width, height, players, room_id, logger

    ##logger.info(f'rooms: {len(rooms)}')

    return redirect(f'/room/{rooms[-1].id}')


@socketio.on('connect')
def connect():
    room_id = 0
    send_updated_map(room_id)


@app.route('/room/<int:room_id>')
@cross_origin()
def play(room_id):

    return render_template('play.html')


@socketio.on('get_map')
def get_map(data):
    room_id = data['room_id']  # TODO: Use socktio.rooms
    send_updated_map(room_id)

@socketio.on('turn')
def turn(data):
    direction = data.get('direction')

    room_id, player_id = int(data.get('room_id')), int(data.get('player_id'))  # Necessary?

    logger.success(f'Input parameters are valid, starting turn;')
    rooms[room_id].turn(player_id, direction)

    send_updated_map(room_id)




def send_updated_map(room_id):
    socketio.emit('map_update', {'map': json.dumps(rooms[room_id].get_map(), cls=UniversalJsonEncoder),
                                 'turn_owner': rooms[room_id].turn_owner_queue[0]})

def socket_send_log(msg):
    socketio.emit('log', msg)

if __name__ == '__main__':
    app.run('0.0.0.0')