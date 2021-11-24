from django.db import models

class Image(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to = 'static/images')
  
  def __str__(self):
        return self.title

class Event(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  number_of_people = models.IntegerField()

  def __str__(self) -> str:
    return self.name