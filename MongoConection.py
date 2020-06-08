import pymongo
import pprint

CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DDBB = CLIENT["G5Proyecto"]
COLLECTION = DDBB["Subvencion"]


query = COLLECTION.find_one()
pprint.pprint(query)

