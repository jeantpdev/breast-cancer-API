import json

def convertir_a_json(edad, menopausia, tumorTamaño, invNodes, nodesCaps, gradoTumor, breast, breastQuead, irradiat, resultado_prueba, precision_modelo):

        rangos_edad = {
            0: "20-29",
            1: "30-39",
            2: "40-49",
            3: "50-59",
            4: "60-69",
            5: "70-79"
        }
        if edad in rangos_edad:
            edad = rangos_edad[edad]

        rangos_menopausia = {
            0: "ge40",
            1: "lt40",
            2: "premeno",  
        }
        if menopausia in rangos_menopausia:
            menopausia = rangos_menopausia[menopausia]

        rangos_tumorTamaño = {
            0: "0-4",
            1: "5-9",
            2: "10-14",
            3: "15-19",
            4: "20-24",
            5: "25-29",
            6: "30-34",
            7: "35-39",
            8: "40-44",
            9: "45-49",
            10: "50-54"
        }
        if tumorTamaño in rangos_tumorTamaño:
            tumorTamaño = rangos_tumorTamaño[tumorTamaño]

        rangos_invNodes = {
            0: "0-2",
            1: "3-5",
            2: "6-8",
            3: "9-11",
            4: "12-14",
            5: "15-17",
            6: "24-26"
        }
        if invNodes in rangos_invNodes:
            invNodes = rangos_invNodes[invNodes]

        rangos_nodesCaps = {
            0: "No",
            1: "Si"
        }
        if nodesCaps in rangos_nodesCaps:
            nodesCaps = rangos_nodesCaps[nodesCaps]

        rangos_gradoTumor = {
            0: "1",
            1: "2",
            2: "3"
        }
        if gradoTumor in rangos_gradoTumor:
            gradoTumor = rangos_gradoTumor[gradoTumor]

        rangos_breast = {
            0: "Izquierda",
            1: "Derecha"
        }
        if breast in rangos_breast:
            breast = rangos_breast[breast]

        rangos_breastQuead = {
            0: "central",
            1: "inferior izquierda",
            2: "superior izquierda",
            3: "inferior derecha",
            4: "superior izquierda"
        }
        if breastQuead in rangos_breastQuead:
            breastQuead = rangos_breastQuead[breastQuead]

        rangos_irradiat = {
            0: "No",
            1: "Si"
        }
        if irradiat in rangos_irradiat:
            irradiat = rangos_irradiat[irradiat]


        datos_json = {
            "age": edad,
            "menopause": menopausia,
            "tumor_size": tumorTamaño,
            "inv_nodes": invNodes,
            "nodes_caps": nodesCaps,
            "deg_malig": gradoTumor,
            "breast": breast,
            "breast_quead": breastQuead,
            "irradiat": irradiat,
            "class": resultado_prueba,
            "precision" : precision_modelo
        }
        datos_insertar = json.dumps(datos_json)

        return datos_insertar
    
def convertir_a_string(texto):
    res = str(texto)
    x = res.replace("[", "")
    y = x.replace("]","")
    return y
