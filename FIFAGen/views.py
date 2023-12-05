from django.shortcuts import render, redirect
from django.contrib.auth import views as views1

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import requests as r
from .models import PlayerInBase, Profile
#from FIFAGen.optimization import base_import
import FIFAGen.optimization as f



#base_import()


# Create your views here.


def create_user(request):
  context={}
  if request.method=="POST":
    u = User.objects.create_user(
      request.POST["username"],
      request.POST["email"],
      request.POST["senha"]
    )
    u.save()
    p = Profile.objects.create(user=u)
    # exemplo = PlayerInBase.objects.get(id=1)
    # p.players.add(exemplo)
    p.save()
    return redirect("/")
  return render(request,"Front/registre.html",context=context)


class Login(views1.LoginView):
  "herda a view do django."

class Logout(views1.LogoutView):
  "herda a view do django."

class PasswordReset(views1.PasswordResetView):
  template_name="registration/senha_reset_form.html"
  email_template_name = 'registration/senha_reset_email.html'


class PasswordResetDone(views1.PasswordResetDoneView):
  template_name="registration/senha_reset_done.html"

class PasswordResetConfirm(views1.PasswordResetConfirmView):
  template_name="registration/senha_reset_confirm.html"

class PasswordResetComplete(views1.PasswordResetCompleteView):
  template_name="registration/senha_reset_complete.html"


def home(request):
  return render(request, 'Front/home.html')

def sobre(request):
  return render(request, 'Front/index.html')
  
def planos(request):
  return render(request, 'Front/planos.html')

def barrapesquisa (request):
  return render(request, 'Front/barrapesquisa.html')

@login_required
def gerador(request):
  data = {}
  team = f.initial_team(request.user)
  for pos in team:
    num = len(team[pos])
    if num > 1:
      for i in range(num):
        new_pos = pos + str(i+1)
        data[new_pos] = team[pos][i]
    else:
      data[pos] = team[pos][0]


  return render(request, 'Front/gerador.html', context=data)

# if ' ' in team[pos][0].playerKeys['name']:
#   data[pos]['name'] = team[pos][0].playerKeys['name'].split(' ')[0]


@login_required
def teste(request):
  context={
    'jogador':'Alguém',
  }
  # jogador = PlayerInBase.objects.get(id=1)

  # jogador=jogador.playerKeys

  # context['jogador']=jogador['name']

  jogador = f.searchByKey("totalStats",473)
  jogador=jogador[0].playerKeys
  context['jogador']=jogador['name']
  team = f.initial_team(request.user)
  context['base']=team
  
  return render(request, 'home.html',context=context)



# FutDB API-Key: c2c45a4c-4b86-471b-8028-0fd73fa978a2
@login_required
def request_tester(request):
  context={}
  
  payload = { "accept" : "application/json", "X-AUTH-TOKEN": "c2c45a4c-4b86-471b-8028-0fd73fa978a2"}
  req = r.get("https://futdb.app/api/players/1", headers=payload)

  context['jogador']=req.json()['player']['name']
  print('\n',req.headers['x-ratelimit-remaining'],'chamadas restantes hoje\n')
  
  return render(request, 'home.html',context=context)


@login_required
def add_to_Profile(request):

  qtdAdd = 0
  p=Profile(user=request.user)
  for i in range(17000,18000):
    if PlayerInBase.objects.filter(id=i).exists():
      exemplo = PlayerInBase.objects.get(id=i)
      p.players.add(exemplo)
      qtdAdd+=1

  print("sucesso. %d adicionados" % qtdAdd)
  return redirect("/")