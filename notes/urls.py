from django.urls import path
from . import views

urlpatterns = [
    path('notes-list/', views.NotesListView.as_view(), name='notes_list'),
    path('note-detail/<int:pk>/', views.DetailNoteView.as_view(), name='note_detail'),
]

