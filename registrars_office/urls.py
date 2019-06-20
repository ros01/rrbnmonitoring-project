from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='registrar_dashboard'),

]
