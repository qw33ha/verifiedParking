import API
import readParkingLots
user_input = input("Enter the location\n")
user_location = API.LocationConvertion(user_input)
database = readParkingLots.readParkingLots("parking-in-city-of-las-vegas-1.csv")
#for x in range(len(database)):
#    print(database[x])
bestfive = API.BestFive(user_location, database)
#for x in range(5):
#    print(database[bestfive[x][0]]['Location'])
destination_string = []
destination_coordinate = []
for x in range(5):
    temp = database[bestfive[x][0]]['Location'].split("\n")[0] + "Las Vegas"
    destination_string.append(temp)
for x in range(5):
    destination_coordinate.append(API.LocationConvertion(destination_string[x]))
API.Demo(destination_coordinate)