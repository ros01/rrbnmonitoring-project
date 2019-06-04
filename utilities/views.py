from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from .choices import price_choices, bedroom_choices, state_choices

from .models import Hospital, License
from django.http import HttpResponse

def index(request):
  hospital = Hospital.objects.all()

  context = {
    'hospital': hospital
  }
  return render(request, 'utilities/hospitals_lookup.html', context)

def licenses(request):
  license = License.objects.all()

  context = {
    'license': license
  }
  return render(request, 'utilities/licenses_lookup.html', context)

def offices(request):
  return render(request, 'utilities/rrbn_offices.html')
