import pymongo
import pandas as pd


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["tiictsystem"]
mycollection = db["users"]
# oneRecord = mycollection.find_one()
# print(oneRecord)

allRecords = mycollection.find()
list_cursor = list(allRecords)

df = pd.DataFrame(list_cursor)
print(df)