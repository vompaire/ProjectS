from django_filters import FilterSet
from .models import Product

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
   class Meta:
       model = Product
       fields = {
           'name': ['icontains'],
           'quantity': ['gt'],
           'price': [
               'lt',  # цена должна быть меньше или равна указанной
               'gt',  # цена должна быть больше или равна указанной
           ],
       }