from flask_restful import Resource, reqparse
from Models.preciocancha import PrecioCanchaModel

class PrecioCanchaController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'descripcion',
            type=str,
            required=True,
            help="Falta descripcion"
        )
        parser.add_argument(
            'monto',
            type=float,
            required=True,
            help="Falta monto"
        )
        parser.add_argument(
            'disponibilidad',
            type=bool,
            required=True,
            help="Falta disponibilidad"
        )
        parser.add_argument(
            'canchita',
            type=int,
            required=True,
            help="Falta canchita"
        )
        data=parser.parse_args()
        insercion=PrecioCanchaModel(data['descripcion'],data['monto'],data['disponibilidad'],data['canchita'])
        try:
            insercion.guardar_en_la_bd()
        except:
            return {'message':'Guardar en la base de datos'}
        return {'message':'Se agrego exitosamente','content':insercion.retornar_json()}