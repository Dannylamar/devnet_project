import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rczb2neOh8r0Cbhj1WWjfMhDwUaqo6X5"

while True:
    orig = input("Stating Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:        " + str(json_data["route"]["distance"]*1.61))
#        print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + ("{:.2f}".format((each["distance"]*1.61 + "km)"))
    print("=============================================")

#while True:
#    orig = input("Starting Location: ")
#    if orig == "quit" or orig == "q":
#        break
#    dest = input("Destination: ")
#if dest == "quit" or dest == "q":
#        break
#("{:.2f}".format