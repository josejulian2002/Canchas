from flask_restful import Resource, reqparse
from Models.opciones import OpcionesModel

class OpcionController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'descripcion',
            type=str,
            required=True,
            help="Falta descripcion"
        )
        data=parser.parse_args()
        insercion=OpcionesModel(data['descripcion'])
        try:
            insercion.guardar_en_la_bd()
        except:
            return {'message':'Error'},500
        return {'message':'Se agrego exitosamente','content':insercion.retornar_json()},201

    def get(self,nombre):
        resultado=OpcionesModel.query.filter_by(opc_desc=nombre).first()
        if resultado:
            return resultado.retornar_json()
        return {'message':'No se encontro'}

class OpcionesController(Resource):
    def get(self):
        resultado=OpcionesModel.query.all()
        if resultado:
            resultadofinal=[]
            for i in resultado:
                resultadofinal.append(i.retornar_json())
            return resultadofinal
        return {'message':'Error'}

        