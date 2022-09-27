from django.contrib import admin
from django.urls import path
from fkip.views import index
from faperta.views import situs
from feb.views import feb
from fh.views import fh
from fisip.views import fisip
from fk.views import fk
from ft.views import ft
from pascasarjana.views import pascasarjana
from profil.views import profil
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', index),
    path('faperta/', situs),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('ft/', ft), 
    path('pascasarjana/', pascasarjana),
    path('profil/', profil),
    path('', views.index),
]