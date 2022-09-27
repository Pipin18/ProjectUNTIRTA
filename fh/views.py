from django.shortcuts import render

# Create your views here.
def fh(request):
    prodi = "Hukum"
    gambaranumum = "Fakultas Hukum Universitas Sultan Ageng Tirtayasa berdiri tahun 1981, tepatnya pada tanggal 1 Oktober 1981 dengan status sebagai STIH Serang yang bertempat di Kresidenan Banten, Jl. K.H. Sam’un dan merupakan embrio lahirnya Universitas Sultan Ageng Tirtayasa Banten. Mulai tahun 1984, STIH Serang di integrasi sesuai dengan SK Mendikbud No. 0596/0/1984, menjadi Fakultas Hukum Universitas Sultan Ageng Tirtayasa yang bertempat di Jl. Raya Jakarta KM. 4 Pakupatan – Serang."

    konteks = {
        'prodi': prodi,
        'gbrumum': gambaranumum,
    }
    return render(request, 'fh.html', konteks)