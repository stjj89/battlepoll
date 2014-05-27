from django.db import models

# Currently only supports 2-way battles


class Voter(models.Model):
    voter_id = models.CharField(max_length=5, primary_key=True)
    vote_weight = models.PositiveIntegerField()

class Battle(models.Model):
	team1 = models.CharField(max_length=100)
	team2 = models.CharField(max_length=100)
	team1_votes = models.PositiveIntegerField()
	team2_votes = models.PositiveIntegerField()

class Vote(models.Model):
	vote_id = models.ForeignKey(Voter)
	battle_id = models.ForeignKey(Battle)
	voted_for_team1 = models.BooleanField()