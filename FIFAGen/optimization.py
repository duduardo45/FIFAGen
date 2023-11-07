import requests as r
from FIFAGen.models import PlayerInBase

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

def initial_team(formation="4-4-2", players=None):
  """
  initialize the user's team for optimization, with a starting formation
  and chooses the appropriate initial players for each position.
  (currently, chooses the highest overall player to start)
  """

  # Players should be a dictionary with the keys being the different positions
  # and the values being a list of players that are in that user's database.


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
  