from __future__ import unicode_literals
from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Coach(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Team(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.firstName + ' ' + self.lastName