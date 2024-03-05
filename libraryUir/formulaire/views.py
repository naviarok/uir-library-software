from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Formulaire
from datetime import date

def get_today_date_str():

  today = date.today()
  day = today.strftime("%d")
  month = today.strftime("%m")
  year = today.strftime("%y")

  return f"{day}/{month}/{year}"

# Create your views here.
def Home(request):
    if request.method == 'POST':
        try:
            firstName = request.POST.get('first', '-')
            lastName = request.POST.get('last', '-')
            code = request.POST.get('code', '-')
            items = request.POST.get('items', '-')
            Formulaire.objects.create(FirstName=firstName, LastName=lastName, Code=code, Items=items, Date=get_today_date_str())
            return redirect('success')
        except:
            return redirect('error')
    return render(request, 'formulaire/index.html')

def Success(request):
    return render(request, 'formulaire/success.html')

def Error(request):
    return render(request, 'formulaire/error.html')


def HomeRedirect(request):
    return redirect('home')