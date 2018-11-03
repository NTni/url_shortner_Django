from django.db import models

class Superheroes(models.Model):
    Name = models.CharField(max_length=100)
    Identity = models.CharField(max_length=100)
    Team = models.CharField(max_length=100)
    Power = models.CharField(max_length=100)
    def __str__(self):
        return self.Name+'-'+ self.Identity

class Vilains(models.Model):
    Name = models.CharField(max_length=100)
    Hero = models.CharField(max_length=100)
    Team = models.CharField(max_length=100)
    def __str__(self):
        return self.Name


