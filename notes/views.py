from django.shortcuts import render

from .models import Notes


def list(request):
    notes = Notes.objects.filter(is_deleted=False).order_by('-created_at')

    context = {
        "notes": notes
    }

    return render(request, "notes/notes_list.html", context)
