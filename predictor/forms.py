from django import forms
from .models import Prediction


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['area','bedrooms','bathrooms','stories','parking']
    