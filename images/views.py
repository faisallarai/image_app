from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://localhost:8000/images/images/')
    image_data = response.json()
    print(image_data)
    return render(request, 'images/home.html', {
        'images': image_data,
    })
