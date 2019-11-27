from base_de_datos import bd


class LocalModel(bd.Model):
    __tablename__ = "t_local"
    loc_id = bd.Column(bd.Integer, primary_key=True)
    loc_nom = bd.Column(bd.String(45))
    loc_lat = bd.Column(bd.DECIMAL(10, 8))
    loc_lng = bd.Column(bd.DECIMAL(10, 8))
    loc_direccion = bd.Column(bd.String(45))
    loc_fono = bd.Column(bd.String(15))

    usu_id=bd.Column(bd.Integer,bd.ForeignKey("t_usuario.usu_id"),nullable=False)
    # usuario=bd.relationship('UsuarioModel',lazy=True,backref='usu')

    canchitas=bd.relationship('CanchitasModel',lazy=True,backref='cancha')


    opcionlocal=bd.relationship('LocalOpcionesModel',lazy=True,backref='localopc')

    def __init__(self,usuario, nombre, latitud, longitud, direccion, telefono):
        self.loc_nom=nombre
        self.loc_lat=latitud
        self.loc_lng=longitud
        self.loc_direccion=direccion
        self.loc_fono=telefono
        self.usu_id=usuario
    
    def retornar_json(self):
        return {
            'nombre':self.loc_nom,
            'latitud':str(self.loc_lat),
            'longitud':str(self.loc_lng),
            'direccion':self.loc_direccion,
            'telefono':self.loc_fono,
            'usuario':self.usu_id
        }
    
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()