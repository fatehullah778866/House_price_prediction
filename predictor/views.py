from django.shortcuts import render
from .forms import PredictionForm
import joblib
import numpy as np
import os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'predictor', 'house_price_prediction.pkl')
model = joblib.load(model_path)

def predict_price(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = [
                data['area'],
                data['bedrooms'],
                data['bathrooms'],
                data['stories'],
                data['parking']
            ]
            predicted_price = model.predict([features])[0]  # Note: features must be nested list

            prediction = form.save(commit=False)
            prediction.predicted_price = predicted_price  # ❗ Correct variable
            prediction.save()

            return render(request, 'predictor/result.html', {'prediction': prediction})
    else:
        form = PredictionForm()
    
    return render(request, 'predictor/predict.html', {'form': form})  # ✅ Always return this at the end
