import json
import requests

api_key="e09fcc99749d2e3493dfe0fb989df11f"
city="kolhapur"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response=requests.get(url)

if response.status_code ==200:
    data=response.json()
    print(json.dumps(data, indent=5))

    with open("weather_data.json","w")as file:
        json.dump(data,file,indent=5)

else:
    print(f"Error:{response.status_code}")
