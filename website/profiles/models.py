from __future__ import unicode_literals
from django.db import models

class Group(models.Model):
    groupName = models.CharField(max_length=100)
    numberOfMembers = models.CharField(max_length=100)

    def __str__(self):
        return self.groupName + '- ' + self.numberOfMembers

class Person(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)



