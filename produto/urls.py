from django.urls import path
from .views import Index, Product

app_name = 'product'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('produtos/<int:pk>', Product.as_view(), name='product_page'),
] 