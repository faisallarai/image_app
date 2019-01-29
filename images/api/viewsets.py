from images.api.serializers import ImageSerializer
from images.models import Image
from rest_framework import generics


class ImageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
