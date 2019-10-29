from flask import Flask, request, redirect
from flask_cors import cross_origin
from room import Room

app = Flask(__name__)

rooms = []


@app.route('/')
@cross_origin()
def index():
    return 'Игрушка'


@app.route('/room/new', methods=['GET'])
@cross_origin()
def create_room():
    map_size = int(request.args.get('size', 10))
    players_number = int(request.args.get('players_number', 2))

    room_id = len(rooms)
    rooms.append(Room(room_id, players_number, 'map-king', map_size))

    return redirect('/room/{}/map'.format(room_id))


@app.route('/room/<int:room_id>/map')
@cross_origin()
def get_map(room_id):
    return rooms[room_id].get_map()


@app.route('/room/<int:room_id>')
@cross_origin()
def get_session_info(room_id):
    return rooms[room_id].get_info()


@app.route('/room/<int:room_id>/join')
@cross_origin()
def join_room(room_id):
    if len(rooms) > room_id:
        return redirect('/room/{}/map'.format(room_id))
    return 'No such room'


if __name__ == '__main__':
    app.run('0.0.0.0', 80)