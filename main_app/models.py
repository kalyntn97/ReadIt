from django.db import models
from django.urls import reverse
from datetime import date, time
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
  title = models.TextField(max_length=100)
  content = models.TextField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  expire_on = models.DateField('Expiry Date', blank=True, null=True, db_index=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  audio = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("note-detail", kwargs={"pk": self.pk})
  
  