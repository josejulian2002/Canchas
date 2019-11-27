from flask import Flask
from flask_restful import Api

from base_de_datos import bd

# from Models.local import LocalModel
from Controllers.local import LocalControllers, LocalesController
# from Models.canchitas import CanchitasModel
from Controllers.canchita import CanchitaController, CanchitasController 
# from Models.tipo import TipoModel
from Controllers.tipo import TipoController,TiposController
# from Models.usuario import UsuarioModel
from Controllers.usuario import UsuarioControllers
# from Models.opciones import OpcionesModel
from Controllers.opciones import OpcionController,OpcionesController
# from Models.preciocancha import PrecioCancha
from Controllers.OpcionesLocal import LocalOpcionesController

from Controllers.preciocancha import PrecioCanchaController
# from Models.reserva import ReservaModel
from Controllers.reserva import ReservaController
from Controllers.valoracion import ValoracionesController

from flask_cors import CORS
app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://1ZrncgxcL1:fCqPUkmwKL@remotemysql.com/1ZrncgxcL1"

api=Api(app)


@app.before_first_request
def iniciar_bd():
    bd.init_app(app)
    # bd.drop_all(app=app)
    bd.create_all(app=app)

api.add_resource(LocalOpcionesController,'/opcioneslocal/agregar')

api.add_resource(OpcionController,'/opcion/agregar','/opcion/buscar/<string:nombre>')

api.add_resource(OpcionesController,'/opciones/traer')

api.add_resource(LocalesController,'/locales/traer')
api.add_resource(LocalControllers,'/local/creado','/local/buscar/<string:nombre>')

api.add_resource(PrecioCanchaController,'/preciocancha/agregar')

api.add_resource(ReservaController,"/reserva/agregar")

api.add_resource(CanchitasController,'/todascanchitas/traer')
api.add_resource(CanchitaController,'/canchita/buscar/<int:id>','/canchita/agregar')

api.add_resource(TipoController,'/tipo/buscar/<string:nombre>','/tipo/agregar')
api.add_resource(TiposController,'/tipos/traer')

api.add_resource(UsuarioControllers,'/usuario/buscar/<string:nombre>','/usuario/agregar')

api.add_resource(ValoracionesController,'/valoraciones/<int:id_local>')

@app.route('/')
def inicio():
    return 'Okidoki'
if __name__=="__main__":
    app.run(debug=True)