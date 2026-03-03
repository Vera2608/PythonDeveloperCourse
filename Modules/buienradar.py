# load the json data from the buienradar api which is located on the https://data.buienradar.nl/2.0/feed/json
import json
import requests
url = "https://data.buienradar.nl/2.0/feed/json"
response = requests.get(url)

data = response.json()
print(data)

# give me the temperature in the city of Amsterdam
print(data)

metingen = data["actual"]["stationmeasurements"]

amsterdam_temp = None
for m in metingen:
    station = m.get("stationname", "").lower()
    regio = m.get("regio", "").lower()
    if "amsterdam" in station or "amsterdam" in regio:
        amsterdam_temp = m.get("temperature")
        amsterdam_time = m.get("timestamp")
        amsterdam_weather = m.get("weatherdescription")
        break

if amsterdam_temp is not None:
    print(f"De temperatuur in Amsterdam is {amsterdam_temp}°C")
    print(f"Time: {amsterdam_time}")
    print(f"Weather: {amsterdam_weather}")
else:
    temp = amsterdam_temp["temperature"]
    print("Geen meetstation voor Amsterdam gevonden in deze JSON.")

