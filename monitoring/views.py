from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from profiles.decorators import monitoring_required
from django.http import HttpResponse
from hospitals.models import Hospital

@login_required
@monitoring_required
def index(request):
    return render (request, 'monitoring/monitoring_dashboard.html')

def list(request):
  hospital = Hospital.objects.all()

  context = {
    'hospital': hospital
  }
  return render(request, 'monitoring/list-applications.html', context)



def vet_application(request, id):
  hospital = get_object_or_404(Hospital, pk=id)
  return render(request, 'monitoring/vet-applications.html', {'hospital': hospital})
