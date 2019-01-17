from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://localhost:8000/images/images/')
    image_data = response.json()
    print(image_data)
    return render(request, 'images/home.html', {
        'images': image_data,
    })


def upload_image(request):
    # If token was already acquired, redirect to home page
    if request.session.get('api_token', False):
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        r = requests.post('http://localhost:8000/images/',
                          data={'title': title, 'width': width})
        if r.status_code == 200:
            response = r.json()
            token = response['token']
            # Save token to session
            request.session['api_token'] = token
        else:
            messages.error(request, 'Authentication failed')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'images/form.html', {})
