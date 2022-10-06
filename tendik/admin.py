from django.contrib import admin
from tendik.models import Tendik 
# Register your models here.

class TendikAdmin(admin.ModelAdmin):
    list_display = ['no', 'nama','nip','jabatan']
    search_fields = ['nip','nama']


admin.site.register(Tendik, TendikAdmin)