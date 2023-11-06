from django.db import models
from django.urls import reverse

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
  expire_on = models.DateField()

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("note-detail", kwargs={"pk": self.pk})
  
  def was_not_updated(self):
    return self.updated_at.date() == self.created_at.date() and self.updated_at.time() == self.created_at.time()
  