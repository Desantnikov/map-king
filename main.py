from flask import Flask, redirect, render_template, request
from flask_cors import cross_origin, CORS
from flask_socketio import SocketIO, join_room, emit, send
import json

from logger import Logger
from room import Room
from config import MAP_SETTINGS, MAP_DEFAULTS, DIRECTIONS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(app, cors_allowed_origins="*")

rooms = []
log = Logger(socketio)



@app.route('/')
@cross_origin()
def index():
    return "Please use /room/new"


@app.route('/room/new', methods=['GET'])
@cross_origin()
def create_room():
    pre_configured = [len(rooms), log]
    settings = [request.args.get(*parameter) for parameter in zip(MAP_SETTINGS, MAP_DEFAULTS)]
    parameters = settings + pre_configured

    rooms.append(Room(*parameters))  # width, height, players, room_id, logger
    log.write(f'Room with ID {rooms[-1].id}  and parameters {{param, val for param, val in parameters}} created:  ')
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
def turn(data):  # get from socket query
    room_id = data.get('room_id')
    player_id = data.get('player_id')
    direction = data.get('direction')

    log.write(f'room_id: {room_id}; player_id: {player_id}; direction: {direction}')

    #if not all([room_id, player_id, direction]):
    #    err = f'Failed to get one of mandatory parameters: room - {room_id}, ' \
    #          f'player - {player_id}, direction - {direction}'
    #    log.error(err)
    #    raise KeyError(err)

    try:
        room_id, player_id = int(room_id), int(player_id)  # Necessary?
        if direction not in DIRECTIONS:
            err = f'Wrong direction: {direction}'
            log.error(err)
            raise ValueError(err)
    except TypeError:
        log.error(f'Got non int-convertable room_id ({roomd_id}) and player_id ({player_id})')


    room = rooms[room_id]
    log.write(f'Player {player_id}; stepped {direction};')

    while room.steps_left:
        log.write(f'Starting steps in loop, {room.steps_left} steps left, player_id {player_id} , room_id {room_id}')
        rooms[room_id].turn(player_id, direction)
        log.write(f'Player {player_id} stepped {direction}; {room.steps_left} steps left')
        send_updated_map(room_id)

    log.write(f'Player {player_id} ends turn')



def send_updated_map(room_id):
    room = rooms[room_id]
    socketio.emit('map_update', {'map': json.dumps(room.get_map()), #default=room.map.serializer),
                                 'turn_owner': room.get_turn_owner()})




def socket_send_log(msg):
    socketio.emit('log', msg)

if __name__ == '__main__':
    app.run('0.0.0.0')