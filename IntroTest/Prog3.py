import requests

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = response.json()

valute = data['Valute']

sorted_valute = sorted(valute.values(), key=lambda x: x['CharCode'], reverse=True)

print(sorted_valute[22]['CharCode'])