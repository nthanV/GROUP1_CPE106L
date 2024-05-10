import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["LAB6_POSTLAB"]

collection = db["tracks"]

document = {
    "Name": "For Those About To Rock (We Salute You)",
    "AlbumId": "Object",
    "MediaTypeId": 1,
    "GenreId": 1,
    "Composer": "Angus Young, Malcolm Young, Brian Johnson",
    "Milliseconds": 343719,
    "Bytes": 11170334,
    "UnitPrice": 0.99
}

result = collection.insert_one(document)

print("Inserted document ID:", result.inserted_id)
