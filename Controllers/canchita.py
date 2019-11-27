from flask_restful import Resource, reqparse

from Models.canchitas import CanchitasModel

class CanchitaController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'tamanio',
            type=str,
            required=True,
            help='Falta tamanio'
        )
        parser.add_argument(
            'foto',
            type=str,
            required=True,
            help="Falta foto"
        )
        parser.add_argument(
            'local',
            type=int,
            required=True,
            help="Falta local"
        )
        parser.add_argument(
            'tipo',
            type=int,
            required=True,
            help="Falta tipo"
        )
        data=parser.parse_args()
        canchita=CanchitasModel(data['tamanio'],data['foto'],data['local'],data['tipo'])
        try:
            canchita.guardar_en_la_bd()
        except:
            return {'message':'Error'},500
        return {'message':'Se agrego exitosamente','content':canchita.retornar_json()},201


    def get(self,id):
        resultado=CanchitasModel.query.filter_by(can_id=id).first()
        # .limit(5)Cuantos quieres
        if resultado:
            return resultado.retornar_json(),200
        else:
            return {'message':'No se encontro cancha con el id '+str(id)},404
        

class CanchitasController(Resource):
    def get(self):
        resultado=CanchitasModel.query.all()
        if resultado:        
            arreglo=[]
            for ele in resultado:
                arreglo.append(ele.retornar_json())
            return arreglo,200
        else:
            return {'message':'No se encontro'},404

