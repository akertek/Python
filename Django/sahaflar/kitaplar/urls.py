from django.contrib import admin
from django.urls import path
from . import views

# buraya include koymadık çünkü burası zaten include edilen module


urlpatterns = [
    # 127.0.0.1:8000/k/
    path("", views. IndexView.as_view(), name="index"),

    # 127.0.0.1:8000/k/talep/
    path('talep/', views.talep, name='talep'),

    # 127.0.0.1:8000/k/arama_sonuclari
    path('arama_sonuclari/', views.arama_sonuclari, name='arama_sonuclari'),

]
