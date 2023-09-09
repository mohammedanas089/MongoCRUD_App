import pymongo
def getClient():
    return pymongo.MongoClient("mongodb://172.17.0.2:27017/")