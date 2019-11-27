from flask_restful import Resource, reqparse
from Models.usuario import UsuarioModel

class UsuarioControllers(Resource):
    def get(self,nombre):
        resultado=UsuarioModel.query.filter_by(usu_nom=nombre).first()
        if resultado:
            return resultado.retornar_json(),200
        else:
            return {'message':'No se encontro'},404 
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'nombre',
            type=str,
            required=True,
            help="Falta el nombre"
        )
        parser.add_argument(
            'apellido',
            type=str,
            required=True,
            help="Falta apellido"
        )
        parser.add_argument(
            'contraseña',
            type=str,
            required=True,
            help="Falta contraseña"
        )
        parser.add_argument(
            'tipo',
            type=str,
            required=True,
            help="Falta tipo"
        )
        parser.add_argument(
            'fono',
            type=str,
            required=True,
            help="Falta DNI"
        )
        parser.add_argument(
            'correo',
            type=str,
            required=True,
            help="Falta correo"
        )
        data=parser.parse_args()
        consulta=UsuarioModel.query.filter_by(usu_mail=data['correo']).first()
        if not consulta:
            try:
                UsuarioModel(data['nombre'],data['apellido'],data['contraseña'],data['tipo'],data['fono'],data['correo']).guardar_en_la_bd()
            except:
                return {'message':'Error'},500
        return {'message':'Se agrego exitosamente'},201
