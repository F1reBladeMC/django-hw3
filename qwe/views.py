from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import SiteSettings

def index(request):
    settings = SiteSettings.objects.first()
    return render(request, 'index.html', {
        'settings': settings
    })

def contacts(request):
    settings = SiteSettings.objects.first()
    return render(request, 'contacts.html', {
        'settings': settings
    })
    