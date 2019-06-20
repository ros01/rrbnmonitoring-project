from django.shortcuts import render
from django.http import HttpResponse

@login_required
def index(request):
    return render (request, 'monitoring/monitoring_dashboard.html')
