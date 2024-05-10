import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["LAB6_POSTLAB"]
collection = db["tracks"]

cursor = collection.find()

for document in cursor:
    for key, value in document.items():
        print(f"{key}: {value}")
    print()