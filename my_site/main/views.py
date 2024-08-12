from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   return render(request, "main/home.html")
def portfolio(request):
   return render(request, "main/portfolio.html")
def contact(request):
   return render(request, "main/contact.html")
def application(request):
   return render(request, "main/application.html")