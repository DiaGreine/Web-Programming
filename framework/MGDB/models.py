from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class App(models.Model):
  name = models.CharField(max_length=50)
  developer = models.CharField(max_length=50)
  categories = models.CharField(max_length=10)
  # tags = ArrayField(models.CharField(max_length=50))
  rank = models.IntegerField(default=999)
  rating = models.FloatField(default=0)
  popularity = models.IntegerField(default=0)
  description = models.TextField()

  imgUrl = models.CharField(max_length=100, default="#")

  def __str__(self):
    return self.name
