from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta: 
        model = Portfolio
        fields = ['ad', 'soyad', 'unvan', 'nomre', 'tehsil;', 'tecrubeleri', 'bacariqlari', 
                  'hobbi', 'dil_bilikleri', 'is_yeri']