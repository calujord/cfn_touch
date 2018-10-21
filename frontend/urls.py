# urls.py

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name="home"),
    url(r'^guardar.json$', GuardarFormView.as_view(), name="home"),
]