import pymongo
class DBConnect(object):
    def configDB(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = client["tiictsystem"]
        # print("Connected to Mongodb: ", self.db)

    
