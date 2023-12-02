import requests as r
from FIFAGen.models import PlayerInBase


def initial_team(user, formation=None):
  """
  initialize the user's team for optimization, with a starting formation
  and chooses the appropriate initial players for each position.
  (currently, chooses the highest overall player to start)
  """
  team = {}
  
  players = user.profile.players.order_by("-playerKeys__totalStats")

  if formation is not None:
    #positions = {'position': 'max for pos'}
    maximum = getMaxPlayers(formation)
    for pos in maximum:
      pos_players = players.filter(playerKeys__position=pos)
      print(pos,len(pos_players))
      for p in pos_players:
        if pos not in team.keys():
          team[pos] = [p]
        elif len(team[pos]) < maximum[pos]:
          team[pos].append(p)
        else:
          break

  
  else:
    f=chooseFormation(user)
    team = initial_team(user,formation=f)

  return team

def chooseFormation(user):

  return "4-3-3"


def getMaxPlayers(formation):

  positions = {}
  
  if formation == "4-3-3":

    positions = { 'GK':1,'CB':2,'LB':1,'RB':1,'CM':3,'LW':1,'RW':1,'ST':1}

  return positions


def quimica(team):

  players = []
  quimica_do_time = {}
  for pos in team:
    players.extend(team.pos)
    quimica_do_time[pos] = []

  for player in players:
    "calcular por equipe, país, e liga"
    id  = player.playerKeys.id
    equipe = player.playerKeys.club
    pais = player.playerKeys.nation
    liga = player.playerKeys.league
    mesma_equipe = 0
    mesmo_pais = 0
    mesma_liga = 0
    quimica = 0
    for p in players:
      if not p.playerKeys.id == id:
        if p.playerKeys.club == equipe:
          mesma_equipe += 1
        if p.playerKeys.nation == pais:
          mesmo_pais += 1
        if p.playerKeys.league == liga:
          mesma_liga += 1

    #checar os limites de cada tipo de quimica
    if mesma_equipe >= 2:
      quimica +=1
      if mesma_equipe >= 4:
        quimica +=1
        if mesma_equipe >= 7:
          quimica +=1
    if mesmo_pais >= 2:
      quimica +=1
      if mesmo_pais >= 5:
        quimica +=1
        if mesmo_pais >= 8:
          quimica +=1
    if mesma_liga >= 3:
      quimica +=1
      if mesma_liga >= 5:
        quimica +=1
        if mesma_liga >= 8:
          quimica +=1
          
    quimica_do_time[player.playerKeys.position].append(quimica)

  return quimica_do_time


def searchByKey(key,value=None):
  """
  searches for a player by their key (name, club, league, overall, etc.)
  """

  key = "playerKeys__" + key
  players = PlayerInBase.objects.order_by(key)
  
  if value is not None: #atualmente ainda não funciona como esperado. Para consertar pode-se fazer caso a caso das chaves.
    key+= "=" + str(value)
    #players = players.filter(key)

    #solução temporária
    players = players.filter(playerKeys__totalStats__gte=value)

  
  return players




def max_players(formation, position): 
  """
  returns the maximum number of players that can be on the team
  for a given position in a specific formation
  """
  possible_positions=["GK","CB","RB","LB","RWB","LWB","CDM","CAM","RM","LM","ST","CF","RF","LF","RW","LW"]

  position_classes={ #preciso aprender como funcionam as restrições posicionais, tanto em relação a quimica
    "GOALKEEPER":["GK"],   # quanto em relação a proibições.
    "DEFENDING":["CB","RB","LB","RWB","LWB"],
    "MIDFIELDER":["CDM","CAM","RM","LM"],
    "FORWARD":["ST","CF","RF","LF","RW","LW"]
  }

  if position=="GK":
    return 1
  
  
  if position not in possible_positions:
    raise ValueError("position must be one of the following: {}".format(possible_positions))

  

  """
  if formation == "4-4-2":
    if position == "GK":
      return 2
    elif position == "CB":
      return 2
    elif position == "LB":
  """



def base_import():

  payload = { "accept" : "application/json", "X-AUTH-TOKEN": "c2c45a4c-4b86-471b-8028-0fd73fa978a2"}

  
  for i in range(1,936):
    
    req = r.get("https://futdb.app/api/players", headers=payload,params={'page':i})
    response=req.json()
    
    for player in response['items']:
      print(player['id'])
      p=PlayerInBase(id = player['id'], playerKeys = player)
      p.save()

  class Player():
    def __init__(self, name, age, position, country, club, league, pace, shooting, passing, dribbling, defending, physical):

      self.name = name
      self.age = age
      self.position = position

      #relevant for calculating chemistry
      self.country = country
      self.club = club
      self.league = league

      #relevant for calculating the overall
      self.pace = pace
      self.shooting = shooting
      self.passing = passing
      self.dribbling = dribbling
      self.defending = defending
      self.physical = physical
      self.overall = (pace + shooting + passing + dribbling + defending + physical) / 7