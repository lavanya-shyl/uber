from django import forms
from .models import Ride




class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        exclude = ['distance', 'fare']  # 👈 Exclude these
        widgets = {
            'ride_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
        
