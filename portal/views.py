from django.shortcuts import render
import requests


def Index(request):
    response = requests.get('http://localhost:8000/api/images/')
    image_data = response.json()
    print(image_data)
    return render(request, 'portal/index.html', {
        'images': image_data,
    })


def Create(request):
    # If token was already acquired, redirect to home page
    if request.session.get('api_token', False):
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        title = request.POST.get('title')
        width = request.POST.get('width')
        height = request.POST.get('height')
        size = request.POST.get('size')
        image = request.POST.get('image')
        r = requests.post('http://localhost:8000/api/images/',
                          data={'title': title,
                                'width': width,
                                'height': height,
                                'image': image,
                                'size': size
                                })
        if r.status_code == 200:
            response = r.json()
            token = response['token']
            # Save token to session
            request.session['api_token'] = token
    else:
        return render(request, 'portal/create.html', {})


def Update(request, image_id):

    print(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        r = requests.put('http://localhost:8000/api/images/' % image_id,
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
        return render(request, 'portal/update.html', {})
