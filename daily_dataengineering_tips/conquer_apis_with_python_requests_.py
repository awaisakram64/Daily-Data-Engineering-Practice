import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY'
response = requests.get(url)
data = response.json()

# Display weather description
description = data['weather'][0]['description']
print(f"Weather in London: {description}")