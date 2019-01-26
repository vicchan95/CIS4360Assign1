from mapbox import Geocoder

geocoder = Geocoder(access_token="pk.eyJ1IjoidmljY2hhbjk1IiwiYSI6ImNqcmR5aHVjZTBteHQ0NHBvem91eHJhZTUifQ.q1igblw6jPxxIiZuz-ivgQ")

response = geocoder.forward("1208 Frankford Ave, Philadelphia, PA 19125")

print(response.status_code)
features = response.json()
print("coordinates: ")
print(features['features'][0]['geometry']['coordinates'][0])
print(features['features'][0]['geometry']['coordinates'][1])