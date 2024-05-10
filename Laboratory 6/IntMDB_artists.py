import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["LAB6_POSTLAB"]
collection = database["artists"] 

artists_data = [
    {"Name": "AC/DC"},
    {"Name": "Accept"}
]

result = collection.insert_many(artists_data)

print("Inserted document IDs:", result.inserted_ids)
