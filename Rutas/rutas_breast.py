from librerias import *
from Controladores.controlador_breast import *

con_breast = BreastControlador()
recibir_datos_prueba = Blueprint('recibir_datos_prueba', __name__)
data_prueba = Blueprint('data_prueba', __name__)

@recibir_datos_prueba.route('/enviar-datos-prueba/', methods=['POST'])
@cross_origin()  
def post_recibir_datos_prueba():
   return con_breast.recibir_datos_prueba()

@data_prueba.route('/data-prueba/', methods=['GET'])
@cross_origin()  
def post_data_prueba():
   return con_breast.data_prueba()
