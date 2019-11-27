from base_de_datos import bd

class PrecioCanchaModel(bd.Model):
    __tablename__ = "t_precioCancha"
    pc_id = bd.Column(bd.Integer, primary_key=True)
    pc_desc = bd.Column(bd.String(45))
    pc_monto = bd.Column(bd.DECIMAL(5,2))
    pc_disponibilidad=bd.Column(bd.Boolean)

    can_id=bd.Column(bd.Integer,bd.ForeignKey('t_canchita.can_id'),nullable=False)

    reserva=bd.relationship('ReservaModel',lazy=True,backref='reservas')
    canchitas = bd.relationship('CanchitasModel', lazy=True)

    def __init__(self,descripcion,monto,disponibilidad,canchita):
        self.pc_desc=descripcion
        self.pc_monto=monto
        self.pc_disponibilidad=disponibilidad
        self.can_id=canchita
    
    def retornar_json(self):
        return {
            'descripcion':self.pc_desc,
            'monto':str(self.pc_monto),
            'disponibilidad':self.pc_disponibilidad,
            'canchita':self.can_id
        }
    
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()
