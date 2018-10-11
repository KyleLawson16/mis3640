import urllib.request
import json

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
city = 'Wellesley'
country_code = 'us'
url = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'.format(
    city=city, country_code=country_code, APIKEY=APIKEY)

print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data['main']['temp'])

# How do we get current temperature?
