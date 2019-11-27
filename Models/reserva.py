from base_de_datos import bd

class ReservaModel(bd.Model):
    __tablename__ = "t_reserva"
    res_id = bd.Column(bd.Integer, primary_key=True)
    res_fechin =bd.Column(bd.DATETIME)
    res_fechfin=bd.Column(bd.DATETIME)
    res_monto=bd.Column(bd.DECIMAL(5,2))
    res_adelanto=bd.Column(bd.DECIMAL(5,2))

    usu_id=bd.Column(bd.Integer,bd.ForeignKey("t_usuario.usu_id"),nullable=False)
    pc_id=bd.Column(bd.Integer,bd.ForeignKey("t_precioCancha.pc_id"),nullable=False)

    valoracion=bd.relationship('ValoracionModel',lazy=True,backref='valoracion')
    precio=bd.relationship('PrecioCanchaModel',lazy=True,backref='precan')

    def __init__(self,fecha_inicio,fecha_fin,monto,adelanto,usuario,precio):
        self.res_fechin=fecha_inicio
        self.res_fechfin=fecha_fin
        self.res_monto=monto
        self.res_adelanto=adelanto
        self.usu_id=usuario
        self.pc_id=precio

    def retornar_json(self):
        return {
            "inicio":self.res_fechin,
            "fin":self.res_fechfin,
            "monto":self.res_monto,
            "adelanto":self.res_adelanto,
            "usuario":self.usu_id,
            "precio":self.pc_id
        }
    
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()