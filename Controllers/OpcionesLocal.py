from flask_restful import Resource, reqparse
from Models.OpcionesLocal import LocalOpcionesModel

class LocalOpcionesController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'local',
            type=int,
            required=True,
            help="Falta local"
        )
        parser.add_argument(
            'opcion',
            type=int,
            required=True,
            help="Falta opcion"
        )

        data=parser.parse_args()
        try:
            LocalOpcionesModel(data['local'],data['opcion']).guardar_en_la_bd()
        except:
            return {'message':'Hubo un error'}
        return {'message':'Se agrego'},200
        