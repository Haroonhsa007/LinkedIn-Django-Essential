from django.shortcuts import render
from django.http import HttpResponseNotFound


from .models import Notes


# *********************************************************** #
#                      Class Based Views                      #
# *********************************************************** #

"""class view"""
"""
from django.view.generic import TemplateView

# for auth us mixins

from django.contrib.auth.mixins import LoginRequiredMixin 
# add it before TemplateView

class ViewTemplate(TemplateView):
    template_name = "test/test.html"
    extra_context = {"context":context}
"""
"""class view urls"""
"""
from django.urls import path
from . import views

urlpatterns = [
    path('viewTemplate/', views.ViewTemplate.as_view(), name='ViewTemplate'),
"""
# *********************************************************** #
#                   Function Based Views                      #
# *********************************************************** #

"""
def list(request):
    notes = Notes.objects.filter(is_deleted=False).order_by("-created_at")

    context = {"notes": notes}

    return render(request, "notes/notes_list.html", context)


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return HttpResponseNotFound("Note not found")

    context = {"note": note}

    return render(request, "notes/note_detail.html", context)

"""
