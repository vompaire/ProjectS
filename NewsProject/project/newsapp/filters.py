from django import forms
from .models import New
from django_filters import *

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewFilter(FilterSet):
    data_public = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), lookup_expr='gt')
    class Meta:
       model = New
       fields = {
           'name': ['icontains'],
           'category': ['exact'],

       }