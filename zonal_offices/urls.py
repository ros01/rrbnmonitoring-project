from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='zonal_offices_dashboard'),

]
