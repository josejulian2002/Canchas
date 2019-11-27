from base_de_datos import bd

class OpcionesModel(bd.Model):
    __tablename__ = "t_opciones"
    opc_id = bd.Column(bd.Integer, primary_key=True)
    opc_desc = bd.Column(bd.String(45))

    # opcionlocal=bd.relationship('LocalOpcionesModel',lazy=True,backref='localopc')

    def __init__(self,descripcion):
        self.opc_desc=descripcion
    
    def retornar_json(self):
        return {
            'id':self.opc_id,
            'descripcion':self.opc_desc
        }
    
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()