from flask_restful import Resource, reqparse

from api.helpers import get_unexpected_error_response
from game_entities import create_new_room, get_all_rooms_list

parser = reqparse.RequestParser()
parser.add_argument('players_amount', help='This field cannot be blank', required=True)
parser.add_argument('width', help='This field cannot be blank', required=True)
parser.add_argument('height', help='This field cannot be blank', required=True)


class Game(Resource):
    #@jwt_required
    def post(self):
        #try:

            data = parser.parse_args()
            print(type(data))
            new_room = create_new_room(data)
            print(data)
            print(data.get('id'))

            response_object = {
                'status': 'Success',
                'message': 'Successfully created new game',
                'game_info': str(new_room),
            }
            return response_object, 200

        #except Exception as e:
        #    return get_unexpected_error_response(e)

    #@jwt_required
    def get(self):
        try:
            response_object = {
                'status': 'Success',
                'message': 'Successfully got rooms list',
                'rooms_info': get_all_rooms_list(),
            }
            return response_object, 200

        except Exception as e:
            return get_unexpected_error_response(e)
