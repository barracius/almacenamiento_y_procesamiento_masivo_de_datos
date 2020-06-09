import pymongo
import pprint
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
            listUrbana.append(element['totalEscolaridad'])
        else:
            listRural.append(element['totalEscolaridad'])
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

