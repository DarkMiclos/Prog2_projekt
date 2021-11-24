from django.db import models

class Image(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to = 'static/images')
  
  def __str__(self):
        return self.title

class Event(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

  def __str__(self) -> str:
      return self.title