import pymongo

#Connect to Database
client = pymongo.MongoClient("mongodb+srv://Andrew:AstroCode@cluster0.jke3h.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client['ParkingLotDB'] #Accessing ParkingLot DB


print(client.list_database_names())

print(db)


### Inserting record into ParkingLot Table
parkingLot = db['ParkingLot']
parkingLot_data = {
    '_id': 1,
    'lon': -34.1,
    'lat':  74.0,
    'capacity': 400,
    'hourly_rate': '$4/hour',
    'reservation_type': 'Public',
    'open': 'Y'
}
#result = parkingLot.insert_one(parkingLot_data)
#print('One post: {0}'.format(result.inserted_id))


for record in parkingLot.find():
    #print(type(record), record)
    print(record)


