from django.urls import path
from my_exchange_app import views


urlpatterns = [
    path('',views.converter, name='exchange')
]