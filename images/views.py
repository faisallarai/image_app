from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render

from images.models import Image
from images.forms import ImageForm


def index(request):

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)


def image_create(request):

    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            print("hi")
            title = form.cleaned_data['title']
            width = form.cleaned_data['width']
            heigth = form.cleaned_data['heigth']
            size = form.cleaned_data['size']
            image = form.cleaned_data['image']
            r = requests.post('http://localhost:8000/api/images/',
                              data={'title': title,
                                    'width': width,
                                    'height': height,
                                    'image': image,
                                    'size': size
                                    })
            if r.status_code == 200:
                response = r.json()
    else:
        form = ImageForm()

    context = {
        'form': form
    }
    return render(request, 'images/image_create.html', context=context)


class ImageList(generic.ListView):
    model = Image
    paginate_by = 10


class ImageDetail(generic.DetailView):
    model = Image


class ImageCreate(CreateView):
    model = Image
    fields = ('title', 'image')


class ImageUpdate(UpdateView):
    model = Image
    fields = '__all__'


class ImageDelete(DeleteView):
    model = Image
    success_url = reverse_lazy('images')
