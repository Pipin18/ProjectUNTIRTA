from django.shortcuts import render

# Create your views here.
def fisip(request):
    judul = ["Program Studi Administrasi Publik", "Program Studi Ilmu Komunikasi", "Program Studi Ilmu Pemerintahan"]
    gambaranumum = "Pada saat Universitas Sultan Ageng Tirtayasa (Untirta) sedang mempersiapkan pengalihan status negeri secara utuh dan menyeluruh dengan ditandainya pengalihan aset dan pengelolaan sumber daya dari Yayasan Pendidikan Tirtayasa kepada pemerintah yang dilaksanakan paling lama dalam kurun waktu tiga tahun. Maka pada tanggal 10 Juni 2003 dikeluarkan Surat Keputusan dari DIRJEN DIKTI DEPDIKNAS dengan nomor 1179/D/ T/2003 tentang izin operasional program studi Ilmu Administrasi Negara dan Ilmu Komunikasi, seiring dengan operasional program studi maka Fakultas Ilmu Sosial dan Ilmu Politik didirikan pada tahun akademik 2002/2003  yang mendapat legitimasi menjadi bagian dari Untirta dengan surat keputusan nomor 124/0/2004 sesuai dengan SOTK."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
        
    }
    return render(request, 'fisip.html', konteks)