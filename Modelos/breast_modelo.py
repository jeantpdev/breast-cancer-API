from librerias import *
from Breast.knn import *
from Modelos.utilidades import *

class Breast():

    def data_prueba(self):
        #texto =  request.json['texto'],
        return jsonify({"resultado_prueba": "texto"})

    
    def recibir_datos_prueba(self):

        datos_usuario_temporal = []

        datos_usuario = {
        'edad': request.json['edad'],
        'menopausia': request.json['menopausia'],
        'tumorTamaño': request.json['tumorTamaño'],
        'invNodes': request.json['invNodes'],
        'nodesCaps': request.json['nodesCaps'],
        'gradoTumor': request.json['gradoTumor'],
        'breast': request.json['breast'],
        'breastQuead': request.json['breastQuead'],
        'irradiat': request.json['irradiat'],
        }

        datos_usuario_temporal.append(datos_usuario)
        edad = datos_usuario['edad']
        menopausia = datos_usuario['menopausia']
        tumorTamaño = datos_usuario['tumorTamaño']
        invNodes = datos_usuario['invNodes']
        nodesCaps = datos_usuario['nodesCaps']
        gradoTumor = datos_usuario['gradoTumor']
        breast = datos_usuario['breast']
        breastQuead = datos_usuario['breastQuead']
        irradiat = datos_usuario['irradiat']
        
        new_data = pd.DataFrame([[edad, menopausia, tumorTamaño, invNodes, nodesCaps, gradoTumor, breast, breastQuead, irradiat]], columns=['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat'])

        resultado_prueba, precision = knn_prediction(new_data)

        if resultado_prueba == "0":
            resultado_prueba = "No hay eventos recurrentes"

        if resultado_prueba == "1":
            resultado_prueba = "Hay eventos recurrentes"

        precision_modelo = str(precision)

        return jsonify({"resultado_prueba": resultado_prueba, "precision_modeo": precision_modelo})
