from base_de_datos import bd
class LocalOpcionesModel(bd.Model):
    __tablename__="t_localopciones"
    localopc_id=bd.Column(bd.Integer,primary_key=True)
    loc_id=bd.Column(bd.Integer,bd.ForeignKey('t_local.loc_id'),nullable=False)
    opc_id=bd.Column(bd.Integer,bd.ForeignKey('t_opciones.opc_id'),nullable=False)
    

    def __init__(self,local,opcion):
        self.loc_id=local,
        self.opc_id=opcion

    def retornar_json(self):
        return {
            'local':self.loc_id,
            'opcion':self.opc_id,
        }
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()