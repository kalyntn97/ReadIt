from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  # path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('about/', views.about, name='about'),
  path('notes/', views.NoteList.as_view(), name='note-index'),
  path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
  path('notes/create/', views.NoteCreate.as_view(), name='note-create'),
  path('notes/<int:pk>/update', views.NoteUpdate.as_view(), name='note-update'),
  path('notes/<int:pk>/delete', views.NoteDelete.as_view(), name='note-delete'),
]