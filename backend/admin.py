# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.http import HttpResponse
from django.utils.encoding import smart_str
from backend.models import Contacto
import csv




class ContactoAdmin(admin.ModelAdmin):
    list_display = ["identificacion", "nombre", "telefono", "movil", "email", "tipo_personeria"]
    actions = ["exportar_como_csv"]

    def exportar_como_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([smart_str(getattr(obj, field)) for field in field_names])
        return response
admin.site.register(Contacto, ContactoAdmin)
