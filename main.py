from flask import Flask, request, redirect, render_template
from flask_cors import cross_origin
from flask_socketio import SocketIO, join_room, emit, send

from models.room import Room
from controllers.room import RoomController

app = Flask(__name__)
socketio = SocketIO(app)

#roomControllers = {}

roomControllers = {}

counter = 0

@app.route('/')
@cross_origin()
def index():  # test
    return render_template('index.html')



@app.route('/room/new', methods=['GET'])
@cross_origin()
def create_room():
    map_size = int(request.args.get('size', 10))
    players_number = int(request.args.get('players_number', 2))
    room_id = len(roomControllers)
    roomControllers[room_id] = RoomController(Room(room_id, players_number, 'map-king', map_size))

    return redirect('/room/{}'.format(room_id))


@app.route('/room/<int:room_id>')
@cross_origin()
def play(room_id):
    socketio.emit('map', roomControllers[room_id].get_map())
    socketio.emit('turn_of', roomControllers[room_id].check_turn())
    socketio.emit('test', ' Play func')
    return render_template('play.html')


@socketio.on('turn')
def turn(room_id, player_id, cells): # get from socket query
    socketio.emit('test', ' turn func')
    cells = ((1,2), (3,4), (5,6))  # parse cords of cells from query
    roomControllers[room_id].turn(player_id, cells)
    return "turn"

@socketio.on('test')
def test(data):  # get from socket query
    socketio.emit('test', '123123123')
    print(data)
    return "12312412"



if __name__ == '__main__':
    app.run('0.0.0.0', 80)