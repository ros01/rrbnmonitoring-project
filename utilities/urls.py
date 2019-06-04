from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='hospitals_lookup'),
    path('licenses', views.licenses, name='licenses_lookup'),
    path('offices', views.offices, name='rrbn_offices'),


]
