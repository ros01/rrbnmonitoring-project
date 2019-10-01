from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='monitoring_dashboard'),
    path('list', views.list, name='list'),
    path('<int:id>/vet_application', views.vet_application, name='vet_application'),

]
