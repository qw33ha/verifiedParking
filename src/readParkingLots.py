## Reading the information about parking lots in Las Vegas
import csv

def reservationTypes(reserve):
    if(len(reserve)==0):
        return 'Public'
    elif('customer' in reserve.lower()):
        return 'Public'
    elif('public' in reserve.lower()):
        return 'Public'
    elif('employee' or 'staff' in reserve.lower()):
        return 'Employee'
    else:
        return reserve

def feeType(fee):
    if(len(fee)==0):
        return 'Y'
    else:
        return fee

def hourlyRate(rate,fee):
    if(fee == 'N'):
        return 'Free'
    elif(len(rate) == 0):
        return 'N/A'
    elif(len(rate) < 4):
        return rate
    else:
        arr = rate.split()
        return arr[1]

def hours(hour):
    if(len(hour) == 0):
        return 'N/A'
    else:
        return hour

def location(address):
    if(';' in address):
        return address[address.find(';')+2:-1]
    else:
        return address

def readParkingLots(file):
    datasetArray = []
    lotInfo = {}

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
        next(read)
        #Make general categories for reseve_type, fee, hourly_rate, time_limit, hour, location
        park_id=0

        for row in read:
            fee = feeType(row[FEE])

            lotInfo[park_id] = {
                'Park ID' : park_id,
                'Capacity' : row[CAPACITY],
                'Reservation Type' : reservationTypes(row[RESERVATION_TYPE]),
                'Fee' : fee,
                "Hourly Rate" : hourlyRate(row[HOURLY_RATE],fee),
                "Maximum Hours" : hours(row[MAX_HOURS]),
                "Hours" : hours(row[HOURS]),
                "Location" : location(row[LOCATION])
            }
            park_id+=1
            
    return lotInfo
#   for i in range(len(lotInfo)):
#        print(lotInfo[i])
#readParkingLots("../Data/parking-in-city-of-las-vegas-1.csv")

