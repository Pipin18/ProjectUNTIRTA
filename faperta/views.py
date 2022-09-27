from django.shortcuts import render

# Create your views here.
def situs(request):
    judul = ["Program Studi Agribisnis", "Program Studi Agroekoteknologi", "Program Studi Ilmu Perikanan", "Program Studi Teknologi Pangan"]
    gambaranumum = "Fakultas Pertanian Universitas Sultan Ageng Tirtayasa merupakan salah satu Fakultas yang ada di lingkungan Universitas Sultan Ageng Tirtayasa yang pada awalnya didirikan berdasarkan SK Ketua Yayasan Pendidikan Tirtayasa Nomor : 020/YPT/VIII/1984 tanggal 31 Agustus 1984 dengan Jurusan Sosial Ekonomi Pertanian Program Studi Sosial Ekonomi Pertanian."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
    }
    
    return render(request,'faperta.html', konteks)