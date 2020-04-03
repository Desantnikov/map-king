from flask import redirect, render_template, request
from flask_cors import cross_origin
from flask_socketio import join_room
from flask_jwt_extended import jwt_required
from loguru import logger

from app import flask_app, socketio
from config import MAP_SETTINGS, MAP_DEFAULTS
from room import Room

rooms = []


@flask_app.route('/')
@jwt_required
@cross_origin()
def index():
    return "Please use /room/new test"


@flask_app.route('/room/new', methods=['GET'])
@cross_origin()
def new_game():
    settings = [request.args.get(*parameter) for parameter in zip(MAP_SETTINGS, MAP_DEFAULTS)]
    parameters = settings + [len(rooms)]  # width, height, players, room_id
    rooms.append(Room(*parameters))

    return redirect(f'/room/{rooms[-1].id}')  # take room with explicid id


@flask_app.route('/room/<int:room_id>')
@cross_origin()
def play(room_id):
    room_id = int(room_id)
    return render_template('play.html', room_id=room_id)


@socketio.on('connect')
def on_connect():
    print(f'\r\n\r\n\r\n CONNECTED \r\n\r\n')
    socketio.emit('test', 'connected!!')


@socketio.on('create_room')
def on_create_room(data):
    username, token, room_id = data.get('username'), data.get('token'), data.get('room_id')
    room_id = int(room_id)
    join_room(room_id)
    socketio.send(f'{username} has entered room {room_id}', room=room_id)
    send_updated_map(room_id)


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
            'turn_owner': current_room.turn_owner_queue[0]}

    logger.info(f'send_upd_map: {map_}')
    socketio.emit('map_update', map_, room=room_id)


if __name__ == '__main__':
    flask_app.run('0.0.0.0')
