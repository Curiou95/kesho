from django.forms import ModelForm
from . import models

class BabeForm(ModelForm):
    class Meta:
        model = models.Babe
        fields = '__all__'



class AddPaymentForm(ModelForm):
    class Meta:
        model = models.Payment
        fields = '__all__'