# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

TIPO_PERSONERIA = (
    ("Persona Natural", "Persona Natural"),
    ("Persona Jurídica", "Persona Jurídica"),
)
class Contacto(models.Model):
    identificacion = models.CharField(max_length=255, verbose_name="Identificación (RUC o C.I.")
    nombre = models.CharField(max_length=255, verbose_name="Nombre y Apellido / Razón Social")
    telefono = models.CharField(max_length=255, verbose_name="Teléfono Fijo")
    movil = models.CharField(max_length=255, verbose_name="Teléfono móvil")
    email = models.EmailField(max_length=255, verbose_name="Correo electrónico")
    tipo_personeria = models.CharField(max_length=255, verbose_name="Tipo de personería", choices=TIPO_PERSONERIA)


    def __unicode__(self):
        return self.nombre