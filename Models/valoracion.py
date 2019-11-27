from base_de_datos import bd

class ValoracionModel(bd.Model):
    __tablename__="t_valoracion"
    val_id=bd.Column(bd.Integer, primary_key=True)
    val_comentario=bd.Column(bd.Text)
    val_estrellas=bd.Column(bd.Integer)

    res_id=bd.Column(bd.Integer,bd.ForeignKey("t_reserva.res_id"),nullable=False)
    reserva = bd.relationship('ReservaModel', lazy=True)

    def __init__(self,comentario,estrella,reserva):
        self.val_comentario=comentario
        self.val_estrellas=estrella
        self.res_id=reserva

    def retornar(self):
        return {
            "comentario":self.val_comentario,
            "estrellas":self.val_estrellas
        }
        

    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()