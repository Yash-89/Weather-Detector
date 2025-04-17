from django.shortcuts import render
import json
from urllib.request import urlopen
from urllib.parse import quote

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city_copy = quote(city)
        res = urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city_copy}&appid=e4f4ba067cb4975f70295e42e3acb407').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinates": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(round(json_data['main']['temp'] - 273.15, 2)) + ' °C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})