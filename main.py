import json

from flask import redirect, render_template, request
from flask_cors import cross_origin
from loguru import logger

from app import flask_app, socketio
from config import MAP_SETTINGS, MAP_DEFAULTS
from json_encoder import UniversalJsonEncoder
from room import Room
from json_encoder import UniversalJsonEncoder
from config import MAP_SETTINGS, MAP_DEFAULTS, DIRECTIONS

rooms = []


@flask_app.route('/')
@cross_origin()
def index():
    return "Please use /room/new"

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

if __name__ == '__main__':
    flask_app.run('0.0.0.0')
