from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    if city:
        api_key = 'fca8c953d2120b8417666b4e0f2ff081'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'temperature': data['main']['temp'],
                'conditions': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return Response(weather)
        else:
            return Response({'error': 'City not found'}, status=404)
    return Response({'error': 'City not provided'}, status=400)

def home(request):
    weather = None
    city = request.GET.get('city')
    if city:
        api_key = 'fca8c953d2120b8417666b4e0f2ff081'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'temperature': data['main']['temp'],
                'conditions': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
    return render(request, 'weather/template.html', {'weather': weather, 'city': city})
