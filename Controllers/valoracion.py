from flask_restful import Resource
from flask_jwt import jwt_required
from Models.valoracion import ValoracionModel
from Models.local import LocalModel


class ValoracionController (Resource):
    @jwt_required()
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'comentario',
            type=str,
            required=True,
            help="Falta Comentario"
        )
        parser.add_argument(
            'estrellas',
            type=int,
            required=True,
            help="Falta estrellas"
        )
        parser.add_argument(
            'reserva',
            type=int,
            required=True,
            help="Falta reserva"
        )
        data=parser.parse_args()
        valoracion=ValoracionModel(data['comentario'],data['estrellas'],data['reserva'])
        try:
            valoracion.guardar_en_la_bd()
        except:
            return{'message':'Hubo un error'}
        return {
            'message':'Se agrego','content':valoracion.res_id
        }

class ValoracionesController(Resource):
    def get(self,id_local):
        sentencia=LocalModel.query.filter_by(loc_id=id_local).first()
        valoracion=[]
        for canchita in sentencia.canchitas:
            for precio in canchita.precio:
                for reserva in precio.reserva:
                    for valoraciones in reserva.valoracion:
                        valoracion.append(valoraciones.retornar())
                    print(reserva.valoracion)
        return valoracion

