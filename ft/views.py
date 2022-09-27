from django.shortcuts import render

# Create your views here.
def ft(request):
    judul = ["Jurusan Teknik Elektro", "Jurusan Teknik Industri", "Jurusan Teknik Kimia", "Jurusan Teknik Mesin", "Jurusan Teknik Metaluri", "Jurusan Teknik Sipil"]
    gambaranumum = "Fakultas Teknik merupakan salah satu fakultas dalam lingkungan Universitas Sultan Ageng Tirtayasa, dimana sejak tahun 2001 Untirta telah menjadi perguruan tinggi negeri berdasarkan Surat Keputusan Presiden Republik Indonesia Nomor 32 tanggal 19 Maret tahun 2001.Kampus FT. Untirta berada dalam Kawasan Industri Cilegon, dimana pada kawasan ini terdapat berbagai macam industri logam berat, kimia, manufacture, engineering dan pembangkit listrik, diantaranya PT. Krakatau Steel & Group, PT. Krakatau Posco, PT. Candra Asri, PT. Asahimas, PT. Tri Polita, PT. PLN (Persero) PLTGU Cilegon, PT. Indonesia Power UBP Suralaya dan sebagainya. Secara geografis, Fakultas Teknik Untirta berada pada gerbang dan lintasan perdagangan Jawa-Sumatera serta lintas perdagangan internasional, yaitu dengan adanya pelabuhan penyeberangan ASDP di Merak serta beberapa pelabuhan internasional diantaranya Cigading, Bojonegara dan Krakatau Bandar Samudra. Secara administratif, Fakultas Teknik Untirta berada di Kota Cilegon dan Provinsi Banten yang terus berkembang."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
    }
    return render(request, 'ft.html', konteks)