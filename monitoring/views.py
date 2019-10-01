from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from profiles.decorators import monitoring_required
from django.http import HttpResponse
from hospitals.models import Centre

@login_required
@monitoring_required
def index(request):
    return render (request, 'monitoring/monitoring_dashboard.html')

def list(request):
  centre = Centre.objects.all()

  context = {
    'centre': centre
  }
  return render(request, 'monitoring/list-applications.html', context)



def vet_application(request, id):
  centre = get_object_or_404(Centre, pk=id)
  return render(request, 'monitoring/vet-applications.html', {'centre': centre})
