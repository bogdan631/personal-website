from django.shortcuts import render
from .forms import TableForm
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
   if request.method=="POST":
      form=TableForm(request.POST)
      form.save()
   form = TableForm()
   context={'form':form}

   return render(request, "main/application.html",context)