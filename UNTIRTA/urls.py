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
from dosen.views import tambah_dosen 
from dosen.views import ubah_dosen 
from dosen.views import hapus_dosen
from mahasiswa.views import mahasiswa
from mahasiswa.views import tambah_mahasiswa
from mahasiswa.views import ubah_mahasiswa
from mahasiswa.views import hapus_mahasiswa
from tendik.views import tendik 
from tendik.views import tambah_tendik
from tendik.views import ubah_tendik
from tendik.views import hapus_tendik
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
    path('dosen', dosen, name='dosen'),
    path('mahasiswa/', mahasiswa, name='mahasiswa'),
    path('tendik/', tendik, name='tendik'),
    path('', views.index),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name="hapus_mahasiswa"),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name="hapus_dosen"),
    path('tambah-tendik/', tambah_tendik, name='tambah_tendik'),
    path('tendik/ubah/<int:id_tendik>', ubah_tendik, name='ubah_tendik'),
    path('tendik/hapus/<int:id_tendik>', hapus_tendik, name="hapus_tendik"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)