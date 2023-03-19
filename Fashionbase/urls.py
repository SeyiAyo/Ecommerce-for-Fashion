from django.urls import path
from . import views

app_name = 'Fashionbase'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('shop.html', views.shop, name = 'shop')
]
