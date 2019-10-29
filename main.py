from flask import Flask, request, redirect, render_template
from flask_cors import cross_origin
from flask_socketio import SocketIO, join_room, emit, send

from room import Room

app = Flask(__name__)
socketio = SocketIO(app)

#ROOMS = {}

rooms = []


@app.route('/')
@cross_origin()
def index():  # test
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('socket connected')

@socketio.on('create')
def on_create(data):
    map_size = data['map_size']
    players_number = data['players']

    room_id = len(rooms)
    rooms.append(Room(room_id, players_number, 'map-king', map_size))

    join_room(room_id)
    emit('message', {'room': room_id})

@socketio.on('join')
def on_join(data):
    room_id = data['room_id']
    if room_id < len(rooms):
        emit('joined', {'map': rooms[room_id].get_map()})
    else:
        emit('joined', {'response': 'Pashol nahui(no such room)'})


@app.route('/room/new', methods=['GET'])
@cross_origin()
def create_room():
    print('/room/new endpoint')

    map_size = int(request.args.get('size', 10))
    players_number = int(request.args.get('players_number', 2))

    room_id = len(rooms)
    rooms.append(Room(room_id, players_number, 'map-king', map_size))

    return redirect('/room/{}/join'.format(room_id))


@app.route('/room/<int:room_id>/map')
@cross_origin()
def get_map(room_id):
    return rooms[room_id].get_map()


#@app.route('/room/<int:room_id>')
#@cross_origin()
#def get_session_info(room_id):
#    return rooms[room_id].get_info()


@app.route('/room/<int:room_id>/join')
@cross_origin()
def join_room(room_id):
    #if len(rooms) > room_id:
    return redirect('/room/{}/map'.format(room_id))
    #return 'No such room'


if __name__ == '__main__':
    app.run('0.0.0.0', 80)