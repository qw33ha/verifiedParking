import pymongo
import readParkingLots
#Connect to Database
client = pymongo.MongoClient("mongodb+srv://Andrew:AstroCode@cluster0.jke3h.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client['ParkingLotDB'] #Accessing ParkingLot DB
parkingLot = db['ParkingLot']

def insertDB(tableName, _id, capacity, reservation_type, fee, hourlyRate, maxHours, hours):
    if (findRecord(tableName, _id) != None):
        print("In table: " + tableName + ", RECORD _id:" + str(_id) + " already exists!")
        return None

    table = db[tableName]
    record = {
        '_id': _id,
        'capacity': capacity,
        'reservation_type': reservation_type,
        'fee': fee,
        'hourly_rate': hourlyRate,
        'maxHours': maxHours,
        'hours': hours,

    }
    result = table.insert_one(record)

    return result #returns recordID

def loadLocalCSVToDatabase(tableName):
    #table = db[tableName]
    database = readParkingLots.readParkingLots("parking-in-city-of-las-vegas-1.csv")
    for key,value in database.items():
        insertDB(tableName, value.get("Park ID"), value.get("Capacity"), value.get("Reservation Type"), value.get("Fee"), 
                 value.get("Hourly Rate"), value.get("Maximum Hours"), value.get("Hours"))


def findRecord(tableName, _id):
    table = db[tableName]

    for record in table.find():
        if (record.get("_id") == _id):
            return record
    
    return None #no existing record

def updateRecord(tableName, _id, newRecord):
    if (findRecord(tableName, _id) == None):
        print("In table: " + tableName + ", RECORD _id:" + str(_id) + " does not exist!")
        return None
    
    table = db[tableName]
    getRecord = { '_id': _id }
    updateRecord = { '$set': newRecord} # newRecord should be:
                                        # { 'attributeName': value, ... }

    table.update_one(getRecord, updateRecord)

def printDB(tableName):
    table = db[tableName]

    for record in table.find():
        print(record)

def getDB(tableName):
    records = []
    table = db[tableName]

    for record in table.find():
        records.append(record)

    return records

# def createOwner(tableName )

def findOwner(tableName, username, password):
    table = db[tableName]
    
    for record in table.find():
        if username == record.get("_id") and password == record.get("password"):
            return True

    return False #owner not found

def modifyOwnerCurrentCapacity(tableName, username, amount):
    table = db[tableName]

    for record in table.find():
        if username == record.get("_id"):
            currentAmount = record.get("current_capacity")
            newAmount = currentAmount + amount
            getRecord = { '_id': username }
            updateRecord = { '$set': {'current_capacity': newAmount}}

            table.update_one(getRecord, updateRecord)

            return


def createTestSampleForParkingLotOwners(tableName):
    table = db[tableName]
    database = readParkingLots.readParkingLots("parking-in-city-of-las-vegas-1.csv")

    counter = 1
    for key, value in database.items():
        username = "Test"+ str(counter)
        password = "pass"+str(counter)
        
        record = {
            '_id': username,
            'password': password,
            'park_id': value.get("Park ID"),
            'current_capacity': 0

        }

        counter+= 1
        result = table.insert_one(record)

    return 
        

def getTopFiveParkingLotCurrentCapacity(tableName, topParkingID ):
    table = db[tableName]

    parkingLotTable = db['ParkingLot']

    trackTopParkingID = []

    tempForParkID = []
    tempForCurrentCapacity = []

    # adding placeholder elements
    for i in range(len(topParkingID)):
        tempForParkID.append(topParkingID[i])
        tempForCurrentCapacity.append(i)
   
    trackTopParkingID.append(tempForParkID)
    trackTopParkingID.append(tempForCurrentCapacity)


    for record in table.find():
        if record.get("park_id") in trackTopParkingID[0]:
            print(record)
            index = trackTopParkingID[0].index(record.get("park_id"))
            trackTopParkingID[1][index] = record.get("current_capacity")

    for record in parkingLotTable.find():
        if (record.get("_id") - 1) in trackTopParkingID[0]:
            index = trackTopParkingID[0].index(record.get("_id") - 1)
            trackTopParkingID[1][index] = int(record.get("capacity")) - trackTopParkingID[1][index]
    print(trackTopParkingID[0])
    print(trackTopParkingID[1])
    return trackTopParkingID[1]




###
def main():
    insertDB('ParkingLot', 1, 200, 'Public', True, 4, 10, '3pm-10pm', -34.2, 74)
    print(findRecord('ParkingLot', 1))

    updateRecord('ParkingLot', 1, { 'capacity': 5000})

    print(findRecord('ParkingLot', 1))
    
    updateRecord('ParkingLot', 1, { 'capacity': 400})
   
    insertDB('ParkingLot', 2, 2400, 'Public', False, 25, 6, '3pm-10pm', -34.9, 60) 
    #updateRecord('ParkingLot', 2, { 'capacity': 20}) #Testing Invalid

    #printDB('ParkingLot')
    print(getDB('ParkingLot'))

    owners = db['ParkingLotOwners']
    record = {
        '_id': 'AndrewB',
        'password': 'test',
        'parkinglot_id': 1,
        'current_capacity': 40,
    }
    result = owners.insert_one(record)
    print(findOwner('ParkingLotOwners', "AndrewB", "test"))
if __name__ == '__main__':
    #main()
    #createTestSampleForParkingLotOwners('ParkingLotOwners')
    loadLocalCSVToDatabase('ParkingLot')
