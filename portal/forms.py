from django import forms


class ImageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    width = forms.IntegerField()
    heigth
