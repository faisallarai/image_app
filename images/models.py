from django.db import models
from django.urls import reverse


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    heigth = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    date_entered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image-detail', args=(str(self.id)))
