from flask_restful import Resource, reqparse
from Models.local import LocalModel

class LocalControllers(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'nombre',
            type=str,
            required=True,
            help="Falta nombre"
        )
        parser.add_argument(
            'latitud',
            type=float,
            required=True,
            help="Falta latitud"
        )
        parser.add_argument(
            'longitud',
            type=float,
            required=True,
            help="Falta longitud"
        )
        parser.add_argument(
            'direccion',
            type=str,
            required=True,
            help="Falta direccion"
        )
        parser.add_argument(
            'telefono',
            type=str,
            required=True,
            help="Falta nombre"
        )
        data=parser.parse_args()
        local=LocalModel(data['nombre'],data['latitud'],data['longitud'],data['direccion'],data['telefono'])
        try:
            local.guardar_en_la_bd()
        except:
            return {
                'message':'Error'
            },500
        return {'message':'Se agrego exitosamente','respuesta':local.retornar_json()},201
    def get(self,nombre):
        resultado=LocalModel.query.filter_by(loc_nom=nombre).all()
        if resultado:
            resultadofinal=[]
            for item in resultado:
                resultadofinal.append(item.retornar_json())
            print(resultado)
            return resultadofinal
        return {'message':'No se encontro'},404

class LocalesController(Resource):
    def get(self):
        resultado=LocalModel.query.all()
        if resultado:
            resultadofinal=[]
            for i in resultado:
                resultadofinal.append(i.retornar_json())
            return resultadofinal
        return {'message':'Error'}

