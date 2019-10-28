from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import Hospital, License, Centre
from django.http import HttpResponse
from .choices import state_choices
from .forms import CentreForm
from django.views import View
from .forms import BasicDetailModelForm, CertUploadModelForm
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.views.generic import (
     CreateView,
     DetailView,
     ListView,
     UpdateView,
     DeleteView
)


@login_required
def licenses(request):
  license = License.objects.all()

  context = {
    'license': license
  }
  return render(request, 'hospitals/licenses_lookup.html', context)

@login_required
def index(request):
   hospital = Hospital.objects.all()

   context = {
     'hospital': hospital
   }
   return render(request, 'hospitals/hospitals_lookup.html', context)



class StartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hospitals/start-hospital-reg.html')



class HospitalCreateView(CreateView):
    template_name = 'hospitals/hospitals_register.html'
    form_class = BasicDetailModelForm
    queryset = Hospital.objects.all() #blog/modelname_list.html
    #success_url = '/'

class HospitalUpdateView(View):

    template_name = 'hospitals/hospital_validate.html'
    template_name1 = 'hospitals/hospital-info-submission-confirmation.html'
    queryset = Hospital.objects.all()
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Hospital, id=id)

        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CertUploadModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
           form = CertUploadModelForm(request.POST, request.FILES, instance=obj)
           if form.is_valid():
              form.save()
           context['object'] = obj
           context['form'] = form
        return render(request, self.template_name1, context)


class HospitalDetailView(View):
    template_name = 'hospitals/hospital-info-submission-confirmation.html'
    queryset = Hospital.objects.all()
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Hospital, id=id)
        return obj





# Send email
#send_mail (
 # 'Hospital Registration Application'
 # 'Your request to register your hospital with RRBN has been succesfully submiteed'
 # 'blueacetechng@gmail.com'
 # ['chigozie_okaro@yahoo.com']
  #fail_silently=False
#)
