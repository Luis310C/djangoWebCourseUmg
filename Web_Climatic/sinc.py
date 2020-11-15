import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "96f9da3898mshce7f0de8f0fdb28p1b5788jsn10da6df9d383"
    }

conn.request("GET", "/weather?lat=0&lon=0&callback=test&id=2172797&lang=null&units=%2522metric%2522%20or%20%2522imperial%2522&mode=xml%252C%20html&q=London%252Cuk", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))