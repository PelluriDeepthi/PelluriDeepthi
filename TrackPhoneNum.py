import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

number = input("Enter the PhoneNumber with the country code:")
phoneNumber = phonenumbers.parse(number)

key = "Enter your API"

yourLocation = geocoder.description_for_number(phoneNumber, 'en')
print("Service provider:" + yourLocation)

yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("Service provider:" + yourServiceProvider)

geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

myMap.save("Location.html")