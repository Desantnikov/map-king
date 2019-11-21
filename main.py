from flask import Flask, request, redirect, render_template
from flask_cors import cross_origin
from flask_socketio import SocketIO, join_room, emit, send
import json

from models.room import Room
from controllers.room import RoomController

app = Flask(__name__)
socketio = SocketIO(app)

#roomControllers = {}

roomControllers = []

counter = 0

@app.route('/')
@cross_origin()
def index():  # test
    return render_template('index.html')



@app.route('/room/new', methods=['GET'])
@cross_origin()
def create_room():
    print('create_room func 1')
    map_size = 10#int(request.args.get('size', 10))
    players_number = 3#int(request.args.get('players_number', 2))
    room_id = len(roomControllers)
    roomControllers.append(RoomController(Room(room_id, players_number, 'map-king', map_size)))

    return redirect('/room/{}'.format(room_id))


@app.route('/room/<int:room_id>')
@cross_origin()
def play(room_id):
    return render_template('play.html')

@socketio.on('join')
def join(data): # get from socket query

    socketio.emit('map', roomControllers[0].get_map())
    socketio.emit('turn_of_player', roomControllers[0].check_turn())

    return "turn"

@socketio.on('turn')
def turn(room_id, player_id, cells): # get from socket query
    socketio.emit('test', ' turn func')
    cells = ((1,2), (3,4), (5,6))  # parse cords of cells from query
    roomControllers[room_id].turn(player_id, cells)
    return "turn"



if __name__ == '__main__':
    app.run()