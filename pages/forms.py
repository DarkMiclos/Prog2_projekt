from django import forms
from django.db.models.fields import EmailField
from django.forms.widgets import NumberInput

class BookingForm(forms.Form):
  name = forms.CharField()
  email = EmailField()
  start_date = forms.DateField()
  end_date = forms.DateField()
  number_of_people = forms.IntegerField()
  price = forms.IntegerField()
