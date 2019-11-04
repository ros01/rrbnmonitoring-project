from django.urls import path, include
from . import views



from .views import (
    StartView,
    #HospitalDetailView,
    #HospitalListView,
    HospitalCreateView,
    HospitalDetailView,
    HospitalUpdateView,
    #HospitalDeleteView,

)

app_name = 'hospitals'
urlpatterns = [
    path('lookup/', views.index, name='hospitals_lookup'),
    path('licenses', views.licenses, name='licenses_lookup'),
    path('start/', views.StartView.as_view(), name='start-reg'),
    #path('register_hospital', views.register_hospital, name='register_hospital'),
    #path('register', views.register, name='register'),
    #path('register_centre', views.centre_register_view, name='register_centre'),
    #path('<int:id>', views.validate, name='validate'),
    #path('', HospitalListView.as_view(), name='hospitals-list'),
    path('register/', HospitalCreateView.as_view(), name='hospitals-register'),
    path('<int:id>/', views.HospitalDetailView.as_view(), name='detail'),
    #path('register/', views.HospitalRegisterView.as_view(), name='hospitals-register'),
    #path('<int:id>/', views.HospitalDetailView.as_view(), name='reg-detail'),
    path('<int:id>/update/', HospitalUpdateView.as_view(), name='update'),
    
    #path('<int:id>/delete/', HospitalDeleteView.as_view(), name='hospitals-delete'),
    #path('<int:id>/consent', views.consent, name='consent'),







]
