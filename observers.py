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
    map_ = {'map': json.dumps(rooms[room_id].get_map(), cls=UniversalJsonEncoder),
            'turn_owner': rooms[room_id].turn_owner_queue[0]}
    logger.info(f'send_upd_map: {map_}')
    socketio.emit('map_update', map_)