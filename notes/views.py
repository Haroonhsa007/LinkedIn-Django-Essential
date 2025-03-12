from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import DetailView, ListView

from .models import Notes


class NotesListView(ListView):
    model = Notes
    template_name = "notes/notes_list.html"
    context_object_name = "notes"
    # option1 
    queryset = Notes.objects.filter(is_deleted=False).order_by("-created_at")

    # option2
    # def get_queryset(self):
    #     return Notes.objects.filter(is_deleted=False).order_by("-created_at")


class DetailNoteView(DetailView):
    model = Notes
    template_name = "notes/note_detail.html"
    context_object_name = "note"

    def get_queryset(self):
        return Notes.objects.filter(is_deleted=False).order_by("-created_at")


class PopularNotesListView(ListView):
    model = Notes
    template_name = None
    context_object_name = "popular_notes"

    def get_queryset(self):
        return Notes.objects.filter(is_deleted=False, likes__gte=1).order_by("-created_at")
