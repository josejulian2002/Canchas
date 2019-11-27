from base_de_datos import bd
import bcrypt


class UsuarioModel(bd.Model):
    __tablename__ = "t_usuario"
    usu_id = bd.Column(bd.Integer, primary_key=True)
    usu_nom = bd.Column(bd.String(45))
    usu_ape = bd.Column(bd.String(45))
    usu_hash = bd.Column(bd.Text)
    usu_salt = bd.Column(bd.Text)
    usu_tipo = bd.Column(bd.String(20))
    usu_fono = bd.Column(bd.String(10))
    usu_mail=bd.Column(bd.Text)

    reserva = bd.relationship('ReservaModel', lazy=True, backref='reserva')
    

    def __init__(self, nombre, ape, password, tipo, dni,correo):
        self.usu_nom = nombre
        self.usu_ape = ape
        password_encriptada = bytes(password, 'utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_encriptada, salt)
        salt = salt.decode('utf-8')
        hashed = hashed.decode('utf-8')
        self.usu_salt = salt
        self.usu_hash = hashed
        self.usu_tipo = tipo
        self.usu_dni = dni
        self.usu_mail=correo
    
    def retornar_json(self):
        return {
            'nombre':self.usu_nom,
            'apellido':self.usu_ape,
            'tipo':self.usu_tipo,
            'fono':self.usu_fono,
            'correo':self.usu_mail
        }

    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()
