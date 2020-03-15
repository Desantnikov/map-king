import json

from flask import redirect, render_template, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from loguru import logger

from app import flask_app, socketio
from config import MAP_SETTINGS, MAP_DEFAULTS
from json_encoder import UniversalJsonEncoder
from room import Room

rooms = []


@flask_app.route('/')
@jwt_required
@cross_origin()
def index():
    return "Please use /room/new test"


@flask_app.route('/room/new', methods=['GET'])
@cross_origin()
def create_room():
    settings = [request.args.get(*parameter) for parameter in zip(MAP_SETTINGS, MAP_DEFAULTS)]
    parameters = settings + [len(rooms)]  # width, height, players, room_id
    rooms.append(Room(*parameters))

    return redirect(f'/room/{rooms[-1].id}')  # take room with explicid id


@flask_app.route('/room/<int:room_id>')
@cross_origin()
def play(room_id):
    return render_template('play.html')


@socketio.on('connect')
def connect():
    room_id = 0
    send_updated_map(room_id)
    logger.info(f'connect:')


@socketio.on('get_map')
def get_map(data):
    room_id = data['room_id']  # TODO: Use socktio.rooms
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

    socketio.emit('test', player_info)


def send_updated_map(room_id):
    map_ = {'map': json.dumps(rooms[room_id].get_map() or not None, cls=UniversalJsonEncoder),
            'turn_owner': rooms[room_id].turn_owner_queue[0]}
    logger.info(f'send_upd_map: {map_}')
    socketio.emit('map_update', map_)


if __name__ == '__main__':
    flask_app.run('0.0.0.0')
