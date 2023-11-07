from django.shortcuts import render
import requests as r
#from FIFAGen.optimization import base_import

#base_import()

# FutDB API-Key: c2c45a4c-4b86-471b-8028-0fd73fa978a2
# Create your views here.
def home(request):
  context={
    'jogador':'Alguém',
  }
  
  return render(request, 'home.html',context=context)


def fut(request):
  context={}
  
  payload = { "accept" : "application/json", "X-AUTH-TOKEN": "c2c45a4c-4b86-471b-8028-0fd73fa978a2"}
  req = r.get("https://futdb.app/api/players/1", headers=payload)

  context['jogador']=req.json()['player']['name']
  print('\n',req.headers['x-ratelimit-remaining'],'chamadas restantes hoje\n')
  
  return render(request, 'home.html',context=context)