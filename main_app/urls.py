from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('notes/', views.NoteList.as_view(), name='note-index'),
  # path('notes/<int:note_id>/', views.note_detail, name='note-detail'),
  path('notes/create/', views.NoteCreate.as_view(), name='note-create'),
]