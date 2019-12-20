from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Tag(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class App(models.Model):
  name = models.CharField(max_length=50)
  developer = models.CharField(max_length=50)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  # tags = ArrayField(models.ForeignKey(Tag))
  # rank = models.IntegerField(default=999)
  # rating = models.FloatField(default=0)
  # popularity = models.IntegerField(default=0)
  description = models.TextField()
  imgUrl = models.CharField(max_length=100, default="#")
  # editorPick = models.BooleanField(default=0)

  def __str__(self):
    return self.name

class Banner(models.Model):
  name = models.CharField(max_length=50)
  id = models.IntegerField(unique=True, validators=[MinValueValidator(0), MaxValueValidator(2)], primary_key=True)
  imgUrl = models.CharField(max_length=100, default="#")

  def __str__(self):
    return self.name

class EditorPick(models.Model):
  id = models.IntegerField(unique=True, validators=[MinValueValidator(0), MaxValueValidator(2)], primary_key=True)
  app = models.ForeignKey(App, on_delete=models.CASCADE, blank=True)
  imgUrl = models.CharField(max_length=100, default="#")

  def __str__(self):
    return self.app.name

class Collection(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class MatchTable(models.Model):
  name = models.ForeignKey(Collection, on_delete=models.CASCADE)
  app = models.ForeignKey(App, on_delete=models.CASCADE)
  rank = models.IntegerField(validators=[MinValueValidator(1)])

  def __str__(self):
    return self.name.name + " : " + self.app.name + " : " + str(self.rank)