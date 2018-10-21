# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView
from backend.models import Contacto


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class GuardarFormView(View):
    def get(self, request, *args, **kwargs):

        Contacto(
            identificacion=self.request.GET.get("ruc"),
            nombre=self.request.GET.get("nombres"),
            telefono=self.request.GET.get("telefono"),
            movil=self.request.GET.get("movil"),
            email=self.request.GET.get("correo"),
            tipo_personeria=self.request.GET.get("tipo"),
        ).save()
        return HttpResponse(json.dumps(dict(success=True)))
