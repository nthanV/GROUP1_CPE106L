import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["LAB6_POSTLAB"]  
collection = database["albums"]  

tracks_data = [
    {"Title": "For Those About To Rock We Salute You", "ArtistId": "Object"},
    {"Title": "Let There Be Rock", "ArtistId": "Object"}
]

result = collection.insert_many(tracks_data)

print("Inserted document IDs:", result.inserted_ids)
