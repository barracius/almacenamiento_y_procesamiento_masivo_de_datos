import pymongo
import pprint
import json

CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DDBB = CLIENT["G5Proyecto"]
COLLECTION = DDBB["Subvencion"]

#La primera consulta a realizar será la comparación de la cifra anual, junto a la cifra mensual del monto total subvencionado a zonas rurales vs zonas urbanas.
def EscolaridadPorArea(anno):
    pipeline = json.loads(
        '[{"$group": {"_id": {"mes": "$mes","anno": "%s", "area": "$area"},"totalEscolaridad": {"$sum": "$escolaridad"},"count": {"$sum": 1}}},{"$sort": {"_id.mes": 1}}]' %(anno))
    cursor = COLLECTION.aggregate(pipeline)
    listUrbana=[]
    listRural=[]

    for element in cursor:
        pprint.pprint(element)

        if(element['_id']['area'] == "Urbano"):
            listUrbana.append(element)
        else:
            listRural.append(element)

    return listUrbana, listRural
