from django.db import models
from django.contrib.auth.models import AbstractUser


from djongo import models as djongo_models

class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)


class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    distance = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)


class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
