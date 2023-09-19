import os 
import requests

city=input('enter the city of which you want to know the weather: ')
#here we will take a free weather api key for getting the weather details from the internet
url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

#here we will use the get method to get the data from the url
r=requests.get(url)
print(r.text)
