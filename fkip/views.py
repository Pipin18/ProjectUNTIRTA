from django.shortcuts import render

# Create your views here.
def index(request):
    judul = ["Jurusan Pendidikan non Formal", "Jurusan Pendidikan Bahasa Indonesia", "Jurusan Pendidikan Bahasa Inggris", "Jurusan Pendidikan Biologi", "Jurusan Pendidikan Matematika", "Jurusan Pendidikan Guru Sekolah Dasar", "Jurusan Pendidikan Guru PAUD", "Jurusan Bimbingan dan Konseling", "Jurusan Pendidikan Fisika", "Jurusan Pendidikan Ilmu Pengetahuan Alam", "Jurusan Pendidikan Kimia", "Jurusan Pendidikan Khusus", "Jurusan Pendidikan Pancasila dan Kwarganegaraan", "Jurusan Pendidikan Sejarah", "Jurusan Pendidikan Seni dan Pertunjukan", "Jurusan Pendidikan Sosiologi", "Jurusan Pendidikan Vokasional Teknik Elektro", "Jurusan Pendidikan Vokasional Teknik Mesin"]
    gambaranumum = "Fakultas Keguruan dan Ilmu Pendidikan (FKIP) Universitas Sultan Ageng Tirtayasa (Untirta) memiliki 18 program studi."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
    }
    return render(request,'fkip.html', konteks)