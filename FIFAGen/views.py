from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'Front/home.html')

def sobre(request):
    return render(request, 'Front/index.html')
def registro(request):
    return render (request, 'Front/registre.html')
def planos(request):
    return render(request, 'Front/planos.html')
def barrapesquisa (request):
    return render(request, 'Front/barrapesquisa.html')