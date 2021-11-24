from django import forms
from django.db.models.fields import EmailField
from django.forms.widgets import NumberInput

class BookingForm(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
  number_of_people = forms.IntegerField()
