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


class ImageList(generic.ListView):
    model = Image
    paginate_by = 10


class ImageDetail(generic.DetailView):
    model = Image


class ImageCreate(CreateView):
    model = Image
    fields = '__all__'


class ImageUpdate(UpdateView):
    model = Image
    fields = '__all__'


class ImageDelete(DeleteView):
    model = Image
    success_url = reverse_lazy('images')
