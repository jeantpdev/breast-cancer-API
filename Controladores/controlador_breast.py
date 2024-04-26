from Modelos.breast_modelo import *

mod_agente = Breast()

class BreastControlador():
    
    def recibir_datos_prueba(self):
        query = mod_agente.recibir_datos_prueba()
        return query
    
    def data_prueba(self):
        query = mod_agente.data_prueba()
        return query