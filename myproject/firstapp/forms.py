from .models import Login_info
from django import forms

class Loging_form(forms.ModelForm):
    class Meta:
        model = Login_info
        fields = '__all__'
