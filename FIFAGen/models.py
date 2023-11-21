from django.db import models
#from django.contrib.auth.models import User

# Create your models here.


class PlayerInBase(models.Model):
  id = models.IntegerField(primary_key=True)
  playerKeys = models.JSONField()


class Profile(models.Model): #modelo que relaciona o usuário com a sua base de jogadores
  user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)
  players = models.ManyToManyField(PlayerInBase,blank=True)


#exemplo de playerKeys com a chave externa "player":
"""
  {
    "player": {
      "id": 1,
      "resourceId": null,
      "resourceBaseId": null,
      "futBinId": null,
      "futWizId": null,
      "firstName": "Kylian",
      "lastName": "Mbappé",
      "name": "Kylian Mbappé",
      "commonName": null,
      "height": 182,
      "weight": 75,
      "gender": "male",
      "birthDate": "1998-12-20",
      "age": 24,
      "league": 16,
      "nation": 18,
      "club": 73,
      "rarity": 1,
      "playStyles": null,
      "playStylesPlus": null,
      "position": "ST",
      "positionAlternatives": null,
      "skillMoves": 5,
      "weakFoot": 4,
      "foot": "right",
      "attackWorkRate": "high",
      "defenseWorkRate": "low",
      "totalStats": 473,
      "totalStatsInGame": 2250,
      "color": "gold",
      "rating": 91,
      "ratingAverage": 78,
      "pace": 97,
      "shooting": 90,
      "passing": 80,
      "dribbling": 92,
      "defending": 36,
      "physicality": 78,
      "paceAttributes": null,
      "shootingAttributes": null,
      "passingAttributes": null,
      "dribblingAttributes": null,
      "defendingAttributes": null,
      "physicalityAttributes": null,
      "goalkeeperAttributes": null
    }
  }
  """
  