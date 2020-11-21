## Reading the information about parking lots in Las Vegas
import csv

def readParkingLots(file):
    datasetArray = []

    #-----Reading all the necessary columns from the dataset-----
    #Column numbers:
    CAPACITY = 5 
    RESERVATION_TYPE = 7
    FEE = 8
    HOURLY_RATE = 9
    MAX_HOURS = 37
    HOURS = 41
    LOCATION = 45


    with open(file, "r") as dataset: 
        read = csv.reader(dataset)

        #Make general categories for reseve_type, fee, hourly_rate, time_limit, hour, location
        park_id = 0
        for row in read:
            datasetArray.append([park_id, int(row[CAPACITY]), row[RESERVATION_TYPE], row[FEE], row[HOURLY_RATE], row[MAX_HOURS], row[HOURS], row[LOCATION]])
            park_id+=1

    for i in range(10):
        print(datasetArray[i])

readParkingLots("../../verifiedParking/Data/parking-in-city-of-las-vegas-1.csv")
