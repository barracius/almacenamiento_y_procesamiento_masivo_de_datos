import pymongo
import pprint



#La primera consulta a realizar será la comparación de la cifra anual, junto a la cifra mensual del monto total subvencionado a zonas rurales vs zonas urbanas.
def query(COLLECTION):
    query = COLLECTION.find_one()
    return query


CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DDBB = CLIENT["G5Proyecto"]
COLLECTION = DDBB["Subvencion"]

