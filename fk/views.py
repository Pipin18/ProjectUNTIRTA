from django.shortcuts import render

# Create your views here.
def fk(request):
    judul = ["Program Studi Kedokteran", "Program Studi Keperawatan S1", "Program Studi Keperawatan D3", "Program Studi S1 GIZI", "Program Studi Ilmu Keolahragaan"]
    gambaranumum = "Fakultas Kedokteran UNTIRTA merupakan fakultas baru di universitas Sultan Ageng Tirtayasa yang terbentuk sejak program studi pendidikan dokter disahkan berdasarkan SK Menteri Riset Teknologi dan Pendidikan Tinggi Republik Indonesia Nomor 283/KPT/I/2019. Program studi Kedokteran Untirta saat ini dibawah pengampuan FK UI."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
    }

    return render(request, 'fk.html', konteks)