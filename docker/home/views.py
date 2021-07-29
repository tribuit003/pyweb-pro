from django.shortcuts import render
from requests import get

# Create your views here.
def index(request):
    ip = get('https://api.ipify.org').text
    return render(request, 'base.html', {'ip':ip})

def cv_page(request):
    return render(request, 'home.html')

def learn_html(request):
    return render(request, 'learn_html.html')