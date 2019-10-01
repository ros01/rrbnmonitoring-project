from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='hospitals_lookup'),
    path('licenses', views.licenses, name='licenses_lookup'),
    path('accept', views.accept, name='accept'),
    path('register', views.register, name='register'),
    path('<int:id>', views.verify, name='verify'),
    path('<int:id>/consent', views.consent, name='consent'),
 

    
    path('search', views.search, name='search'),






]
