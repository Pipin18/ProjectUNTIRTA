from django.shortcuts import render

# Create your views here.
def feb(request):
    judul = ["Program Sarjana Managemen", "Program Sarjana Akuntansi", "Program Sarjana Ilmu Ekonomi Pembangunan", "Program Sarjana Ekonomi Syariah", "Program Diploma III Akuntansi", "Program Diploma III Marketing", "Program Diploma III Perpajakan", "Program Diploma III Keuangan Perbankan"]
    gambaranumum = "Fakultas Ekonomi dan Bisnis merupakan fakultas favorit di Untirta. Sebab, program studi manajemen selalu menjadi program studi yang paling diminati. Buktinya, pada tahun 2019/2020 jumlah mahasiswa baru FEB Untirta mencapai 551 orang yang mana jumlah ini menjadi peringkat ketiga fakultas yang memiliki jumlah mawasiswa terbanyak setelah FKIP dan FT."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
    }
    return render(request, 'feb.html', konteks)