from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from fkip.views import index
from faperta.views import situs
from feb.views import feb
from fh.views import fh
from fisip.views import fisip
from fk.views import fk
from ft.views import ft
from pascasarjana.views import pascasarjana
from profil.views import profil
from dosen.views import dosen
from mahasiswa.views import mahasiswa
from tendik.views import tendik 
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
    path('dosen/', dosen),
    path('mahasiswa/', mahasiswa),
    path('tendik/', tendik),
    path('', views.index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)