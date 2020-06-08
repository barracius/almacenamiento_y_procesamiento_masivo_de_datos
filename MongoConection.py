import pymongo
import pprint



def hola():
    hola = "hola"
    return hola

def main():
    CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
    DDBB = CLIENT["G5Proyecto"]
    COLLECTION = DDBB["Subvencion"]

    query = COLLECTION.find_one()
    pprint.pprint(query)

if __name__ == '__main__':
    main()