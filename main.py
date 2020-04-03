import os
import sys

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required
from flask_socketio import SocketIO, join_room
from loguru import logger

from api import api_init
from db import db_init, jwt_init
from game_entities import rooms, create_new_room

logger.add(sys.stdout, colorize=True)

flask_app = Flask(__name__)
api = api_init(flask_app)
db = db_init(flask_app)
jwt = jwt_init(flask_app)

flask_app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY', 'add_env_var')

CORS(flask_app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(flask_app, cors_allowed_origins="*", log=logger, channel='')


@flask_app.route('/')
@jwt_required
@cross_origin()
def index():
    return "Please use /room/new test"


@flask_app.route('/room/new', methods=['GET', 'POST'])
@cross_origin()
def new_game():
    if request.method == 'GET':
        return render_template('new_game.html')

    if request.method == 'POST':
        request_data = {'players_amount': int(request.form.get('players_amount')),
                        'width': int(request.form.get('width')),
                        'height': int(request.form.get('height'))}

        room_id = create_new_room(request_data).id
        return f'room {room_id} with {request_data} parameters created'


@flask_app.route('/room/<int:room_id>')
@cross_origin()
def play(room_id):
    room_id = int(room_id)
    return render_template('play.html', room_id=room_id)


@socketio.on('connect')
def on_connect():
    print(f'\r\n\r\n\r\n CONNECTED \r\n\r\n')
    socketio.emit('test', 'connected!!')


@socketio.on('create_room') # TODO: Rename on_join_to_room
def on_create_room(data):
    # enter socketIO room with same ID as game room's id
    user_id, username, token, room_id = int(data.get('user_id')), int(data.get('username')), \
                                        int(data.get('token')), int(data.get('room_id'))
    cur_room = rooms[room_id]
    join_room(cur_room.id)

    cur_room.new_player_connected(user_id, username)

    socketio.emit('test', f'{username} has entered room; Please wait: '
                          f'{cur_room.count_free_slots()}', room=room_id)

    if cur_room.ready_to_start():
        send_updated_map(room_id)
    else:
        socketio.emit('map_update', f'Not all players present; {cur_room.count_free_slots()} '
                                    f'players left to total amount of {cur_room.players_amount}', room=room_id)


@socketio.on('get_map')
def get_map(data):
    room_id = int(data.get('room_id'))
    send_updated_map(room_id)
    logger.info(f'get_map data: {data}')


@socketio.on('turn')
def turn(data):
    direction = data.get('direction')

    room_id, player_id = int(data.get('room_id')), int(data.get('player_id'))  # Necessary?

    logger.success(f'Input parameters are valid, starting turn;')
    rooms[room_id].turn(player_id, direction)

    send_updated_map(room_id)
    player_info = ''
    for player in rooms[room_id].players:  # Debug
        player_info = player_info + f'Player {player.id} has {player.health} HP'

    socketio.emit('test', player_info, room=room_id)


def send_updated_map(room_id):
    room_id = int(room_id)
    current_room = rooms[room_id]

    map_ = {'map': current_room.map.get_dict(),
            'turn_owner': current_room.turn_owner_queue[0] }

    logger.info(f'send_upd_map: {map_}')
    socketio.emit('map_update', map_, room=room_id)


if __name__ == '__main__':
    flask_app.run('0.0.0.0')
