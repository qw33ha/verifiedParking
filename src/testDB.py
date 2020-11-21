import pymongo


client = pymongo.MongoClient("mongodb+srv://Andrew:AstroCode@cluster0.jke3h.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test


print(client.list_database_names())
