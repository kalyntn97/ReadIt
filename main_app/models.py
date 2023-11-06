from django.db import models

# Create your models here.
# class TimeStampMixin(models.Model):
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#   class Meta:
#     abstract: True

class Note(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  expire_on = models.DateTimeField()

  def __str__(self):
    return self.title