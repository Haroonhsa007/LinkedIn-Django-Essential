from django.urls import path
from . import views

urlpatterns = [
    path('notes-list/', views.list, name='notes_list'),
    path('note-detail/<int:pk>/', views.detail, name='note_detail'),
    
    # Add more paths here as needed, e.g.,
    # path('create/', views.create, name='create_note'),
]

