import pymongo
import pandas as pd


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["tiictsystem"]
# print(db)

mycollection = db["users"]
# print(mycollection)

# oneRecord = mycollection.find_one()
# print(oneRecord)

allRecords = mycollection.find()
# print(allRecords)

# for row in allRecords:
#     print(row)

list_cursor = list(allRecords)
# print(list_cursor)

df = pd.DataFrame(list_cursor)
print(df)