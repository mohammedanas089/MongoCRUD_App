import pymongo
def getClient():
    return pymongo.MongoClient("mongodb://localhost:27017/")