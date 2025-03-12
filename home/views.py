from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.dateformat import format

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = format(timezone.now(), 'Y-m-d H:i:s')
        return context