from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from django.http import HttpResponse
import time


class HomeView(TemplateView):
    template_name = "index.html"


class InfoView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'info.html')