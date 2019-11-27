from base_de_datos import bd

class TipoModel(bd.Model):
    __tablename__ = "t_tipo"
    tipo_id = bd.Column(bd.Integer, primary_key=True)
    tipo_desc = bd.Column(bd.String(45), nullable=True)

    canchitas = bd.relationship('CanchitasModel', lazy=True)
    # backref declra una propiedad en la clase solamente necesitaria canchita.tipo

    def __init__(self, descripcion):
        self.tipo_desc = descripcion

    def retornar_json(self):
        return {
            'id': self.tipo_id,
            'descripcion': self.tipo_desc
        }

    def retornar_json_con_nombre_local(self):
        nombres = []
        for canchita in self.canchitas:
            nombres.append({"nombre":canchita.local.loc_nom,"lat":str(canchita.local.loc_lat),"lng":str(canchita.local.loc_lng)})
        canchita=[]
        for nombre in nombres:
            if nombre not in canchita:
                canchita.append(nombre)
        return canchita

    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()
