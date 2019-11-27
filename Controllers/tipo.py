from flask_restful import Resource, reqparse
from Models.tipo import TipoModel

class TipoController(Resource):
    def get(self,nombre):
        resultado=TipoModel.query.filter(TipoModel.tipo_desc.like('%'+nombre+'%')).all()
        if resultado:
            resultadofinal=[]
            for i in resultado:
                resultadofinal.append(i.retornar_json_con_nombre_local())
            return resultadofinal
                
        else:
            return {'message':'No se encontro'},404
    
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'descripcion',
            type=str,
            required=True,
            help="Falta descripcion"
        )
        data=parser.parse_args()
        consulta=TipoModel.query.filter_by(tipo_desc=data['descripcion']).first()
        if not consulta:
            consulta=TipoModel.query.filter_by()
            insercion=TipoModel(data['descripcion'])
            try:
                insercion.guardar_en_la_bd()
            except:
                return {'message':'Error'},500
            return {'message':'Se agrego exitosamente'},201
        return {'message':'Ya hay un tipo creado con es descripcion'},412

class TiposController(Resource):
    def get(self):
        resultado=TipoModel.query.all()
        if resultado:
            resultadofinal=[]
            for i in resultado:
                resultadofinal.append(i.retornar_json())
            return resultadofinal
        return {'message':'Error'}
        
