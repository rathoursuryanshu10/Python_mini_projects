from geopy.geocoders import Nominatim
geolocator=Nominatim(user_agent="geoapiExercises")
place=input("Enter the City Name:: ")
location=geolocator.geocode(place)
print(location)
