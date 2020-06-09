import pymongo
import json

CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DDBB = CLIENT["G5Proyecto"]
COLLECTION = DDBB["Subvencion"]

def EscolaridadPorArea(anno):
    pipeline = json.loads('[{"$group": {"_id": {"mes": "$mes","anno": "%s", "area": "$area"},"totalEscolaridad": {"$sum": "$escolaridad"},"count": {"$sum": 1}}},{"$sort": {"_id.mes": 1}}]' %(anno))
    cursor = COLLECTION.aggregate(pipeline)
    listUrbana=[]
    listRural=[]

    for element in cursor:
        if(element['_id']['area'] == "Urbano"):
            listUrbana.append(element)
        else:
            listRural.append(element)
    return listUrbana, listRural

def EscolaridadPromedioPorArea(anno):
    pipeline = json.loads('[{"$group": {"_id": {"area": "$area","anno": "%s","mes": "$mes"},"escolaridad": {"$sum": "$escolaridad"},"count": {"$sum": 1}}}'
                         ', {"$project":{"escolaridadPorInstritucion": {"$divide":["$escolaridad", "$count"]}}},'
                         '{"$sort": {"_id.mes": 1}}]' %(anno))
    cursor = COLLECTION.aggregate(pipeline)
    listUrbana = []
    listRural = []

    for element in cursor:
        if (element['_id']['area'] == "Urbano"):
            listUrbana.append(element)
        else:
            listRural.append(element)
    return listUrbana, listRural

def EscolaridadPorRegion(anno):
    pipeline = json.loads('[{"$group": {"_id": {"mes": "$mes","anno": "%s", "area": "$area", region: "$reg_cod"},"escolaridad": {"$sum": "$escolaridad"},"count": {"$sum": 1}}},{"$sort": {"_id.mes": 1}}]'%(anno))
    cursor = COLLECTION.aggregate(pipeline)
    listUrbana = []
    listRural = []

    for element in cursor:
        if (element['_id']['area'] == "Urbano"):
            listUrbana.append(element)
        else:
            listRural.append(element)
    return listUrbana, listRural

def EscolaridadPorAreaMes(anno,mes):
    pipeline=[
    {
        '$match': {
            'mes': mes,
            'anno': anno
        }
    }, {
        '$group': {
            '_id': {
                'mes': '$mes',
                'anno': '$anno',
                'area': '$area'
            },
            'totalEscolaridad': {
                '$sum': '$escolaridad'
            }
        }
    }
]
    cursor = COLLECTION.aggregate(pipeline)
    listUrbana = []
    listRural = []


    for element in cursor:
        print(element)
        if (element['_id']['area'] == "Urbano"):
            listUrbana.append(element)
        else:
            listRural.append(element)

    return listUrbana, listRural



def DiferenciaAnnoConAnnoAnterior(anno, mes):
    annoAnterior = anno-1
    listUrbana1, listRural1 = EscolaridadPorAreaMes(anno, mes)
    listUrbana2, listRural2 = EscolaridadPorAreaMes(annoAnterior, mes)

    print("rural1: ", listRural1)
    print("rural2: ", listRural2)

    differenciaUrbana = listUrbana1[0]['totalEscolaridad']-listUrbana2[0]['totalEscolaridad']
    listUrbanaT = []
    listUrbanaT.append(differenciaUrbana)

    differenciaRural = listRural1[0]['totalEscolaridad']-listRural2[0]['totalEscolaridad']
    listRuralT= []
    listRuralT.append(differenciaRural)



    return listUrbanaT, listRuralT


print(DiferenciaAnnoConAnnoAnterior(2016, 6))
