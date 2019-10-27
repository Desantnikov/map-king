from flask import Flask, request, redirect
from flask_cors import cross_origin
from room import Room

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

rooms = []


@app.route('/')
@cross_origin()
def index():
    return 'Игрушка'



@app.route('/room/new', methods = ['GET'])
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


@app.route('/room/join/<int:room_id>')
@cross_origin()
def join_room(room_id):
    return {'user_id': 4234, 'max_players': 4, 'cur_player': 2}

if __name__ == '__main__':
    app.run('0.0.0.0', 80)