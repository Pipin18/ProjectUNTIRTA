from multiprocessing import context
from django.shortcuts import render, redirect
from tendik.forms import FormTendik
from tendik.models import Tendik
from django.contrib import messages
# Create your views here.

def hapus_tendik(request, id_tendik):
    tendik = Tendik.objects.filter(id=id_tendik)
    tendik.delete()
    messages.success(request, "Data Berhasil di Hapus!")
    
   
    return redirect('tendik')



def ubah_tendik(request, id_tendik):
    tendik = Tendik.objects.get(id=id_tendik)
    templates ='ubah-tendik.html'
    if request.POST:
        form = FormTendik(request.POST, instance=tendik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil di Ubah!")
            return redirect('ubah_tendik', id_tendik=id_tendik)
    else:
        form = FormTendik(instance=tendik)
        context = {
            'form': form,
            'tendik': tendik,
        }
    return render(request, templates, context)


def tambah_tendik(request):
    if request.POST:
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data berhasil disimpan"

            context = {
                'form': form,
                'pesan' : pesan, 
            }
            
            return render(request, 'tambah-tendik.html', context)

    else:
         form = FormTendik()

         context = {
            'form': form,

         }
    return render(request,"tambah-tendik.html", context)

    
def tendik (request):
    context = {
        'educator': Tendik.objects.all()

    }
    return render(request,"tendik.html", context)

 