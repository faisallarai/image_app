from django.test import TestCase

from images.models import Image


class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Image.objects.create(title='logo', width=100,
                             heigth=100, size=10)

    def test_title_label(self):
        image = Image.objects.get(id=1)
        field_label = image._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        image = Image.objects.get(id=1)
        max_length = image._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_width_label(self):
        image = Image.objects.get(id=1)
        field_label = image._meta.get_field('width').verbose_name
        self.assertEquals(field_label, 'width')

    def test_heigth_label(self):
        image = Image.objects.get(id=1)
        field_label = image._meta.get_field('heigth').verbose_name
        self.assertEquals(field_label, 'heigth')

    def test_size_label(self):
        image = Image.objects.get(id=1)
        field_label = image._meta.get_field('size').verbose_name
        self.assertEquals(field_label, 'size')

    def test_object_name(self):
        image = Image.objects.get(id=1)
        object_name = str(image)
        self.assertEquals(object_name, f'{image.title}')
