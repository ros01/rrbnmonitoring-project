from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
#from .choices import price_choices, bedroom_choices, state_choices

from .models import Hospital, License, Centre
from django.http import HttpResponse
from .choices import state_choices

@login_required
def index(request):
  hospital = Hospital.objects.all()

  context = {
    'hospital': hospital
  }
  return render(request, 'hospitals/hospitals_lookup.html', context)

@login_required
def licenses(request):
  license = License.objects.all()

  context = {
    'license': license
  }
  return render(request, 'hospitals/licenses_lookup.html', context)

def register(request):

  context = {
            'state_choices': state_choices,
            }

  if request.method == 'POST' :
      if request.POST['centre_name'] and request.POST['rc_number'] and request.POST['phone'] and request.POST['email'] and request.POST['state'] and request.POST['city'] and request.POST['address'] and request.FILES['cac_certificate'] and request.FILES['practice_license']:
          centre = Centre()
          centre.centre_name = request.POST['centre_name']
          centre.rc_number = request.POST['rc_number']
          centre.phone = request.POST['phone']
          centre.email = request.POST['email']
          centre.state = request.POST['state']
          centre.city = request.POST['city']
          centre.address = request.POST['address']
          centre.cac_certificate = request.FILES['cac_certificate']
          centre.practice_license = request.FILES['practice_license']
          centre.save()

          return redirect('/hospitals/' + str(centre.id))
      else:
          return render(request, 'hospitals/register-hospital-info.html',{'error':'All fields are required.'})
  else:
      return render(request, 'hospitals/register-hospital-info.html', context)


def accept(request):
    return render(request, 'hospitals/start-hospital-reg.html')

def verify(request, id):
  centre = get_object_or_404(Centre, pk=id)
  return render(request, 'hospitals/validate-hospital-info.html', {'centre': centre})
  if request.method == 'POST':
      if request.FILES['cac_certificate'] and request.FILES['practice_license']:
          centre = Centre()
          centre.cac_certificate = request.FILES['cac_certificate']
          centre.practice_license = request.FILES['practice_license']
          centre.instance.save()

      return render(request, 'hospitals/validate-hospital-info.html')

  else:
      return render(request, 'hospitals/validate-hospital-info.html',{'error':'All fields are required.'})



def consent(request, id):

    centre = get_object_or_404(Centre, pk=id)
    return render(request, 'hospitals/hospital-info-submission-confirmation.html', {'centre': centre})


# Send email
#send_mail (
 # 'Hospital Registration Application'
 # 'Your request to register your hospital with RRBN has been succesfully submiteed'
 # 'blueacetechng@gmail.com'
 # ['chigozie_okaro@yahoo.com']
  #fail_silently=False
#)
def search(request):

    context = {
            'state_choices': state_choices,
            }
    return render(request, 'hospitals/search.html', context)
