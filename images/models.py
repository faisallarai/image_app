from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    height = models.IntegerField()
    width = models.IntegerField()
    size = models.IntegerField()
    date_entered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
