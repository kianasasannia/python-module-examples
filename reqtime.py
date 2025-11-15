import requests
import json
from PIL import Image


response = requests.get("https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873&timezone=UTC&date=today")

api = json.loads(response.content)
print(api)