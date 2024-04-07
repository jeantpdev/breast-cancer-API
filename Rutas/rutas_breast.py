from librerias import *
from Controladores.controlador_breast import *

con_breast = BreastControlador()

todo = Blueprint('todo', __name__)

@todo.route('/enviar-datos-prueba/', methods=['POST'])
@cross_origin()  
def post_recibir_datos_prueba():
   return con_breast.recibir_datos_prueba()

@todo.route('/data-prueba/', methods=['GET'])
@cross_origin()  
def post_data_prueba():
   return con_breast.data_prueba()
