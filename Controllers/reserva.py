from Models.reserva import ReservaModel
from flask_restful import Resource, reqparse
class ReservaController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'inicio',
            type=str,
            required=True,
            help="Falta inicio"
        )
        parser.add_argument(
            'fin',
            type=str,
            required=True,
            help="Falta final"
        )
        parser.add_argument(
            'monto',
            type=float,
            required=True,
            help="Falta monto"
        )
        parser.add_argument(
            'adelanto',
            type=float,
            required=True,
            help="Falta adelanto"
        )
        parser.add_argument(
            'usuario',
            type=int,
            required=True,
            help="Falta usuario"
        )
        parser.add_argument(
            'precio',
            type=int,
            required=True,
            help="Falta precio"
        )
        data=parser.parse_args()
        validar=ReservaModel.query.filter_by(pc_id=data['precio']).all()
        from datetime import datetime
        fechaintroducidainicio=datetime.strptime(data['inicio'],'%Y-%m-%d %H:%M')
        fechaintroducidafin=datetime.strptime(data['fin'],'%Y-%m-%d %H:%M')
        print(fechaintroducidainicio)
        print(fechaintroducidafin)
        for sentencia in validar:
            fehaencontradainicio=sentencia.res_fechin
            fechaencontradafin=sentencia.res_fechfin
            if (fechaintroducidainicio>=fehaencontradainicio and fechaintroducidafin<fechaencontradafin) or (fechaintroducidafin>fehaencontradainicio and fechaintroducidafin<=fechaencontradafin) or (fehaencontradainicio==fechaintroducidainicio and fechaintroducidafin==fechaencontradafin) or (fechaintroducidainicio<fehaencontradainicio and fechaencontradafin>fechaintroducidafin):
                return {'message':'Ya hay una reserva en ese horario'}
            # if (fechaintroducidainicio<fechaencontradafin):
            #     return 'no hay'
            print(fehaencontradainicio,fechaencontradafin)
            print(sentencia)
        insercion=ReservaModel(data['inicio'],data['fin'],data['monto'],data['adelanto'],data['usuario'],data['precio'])
        try:
            insercion.guardar_en_la_bd()
        except:
            return {'Message':'Hubo un error'}
        return {'content':insercion.retornar_json()}

