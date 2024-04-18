from django.forms import ModelForm
from . import models

class AddBabeForm(ModelForm):
    class Meta:
        model = models.Babe
        fields = '__all__'



