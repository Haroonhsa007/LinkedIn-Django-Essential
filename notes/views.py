from django.shortcuts import render
from django.http import HttpResponseNotFound


from .models import Notes


def list(request):
    notes = Notes.objects.filter(is_deleted=False).order_by('-created_at')

    context = {
        "notes": notes
    }

    return render(request, "notes/notes_list.html", context)


def detail(request, pk ):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return HttpResponseNotFound("Note not found")
    
    context = {
        "note" : note
    }
    
    return render(request, "notes/note_detail.html", context)