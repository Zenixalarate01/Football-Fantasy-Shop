Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
Pertama, kita membuat direktori baru di penyimpanan lokal dan juga github
Kedua, Menghubungkan direktori lokal dan github agar menjaga konsistensi
Ketiga, saya melakukan branching agar dapat menyimpan perubahan tanpa harus mengubah file-file di branch utama
Keempat, saya mengaktifkan virtual environment agar mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada di komputer.
Kelima, saya menyiapkan Dependencies melalui requirements.txt lalu membuat proyek Django
Keenam, membuat file variable environment yang memungkinkan kode yang sama berjalan di environment berbeda tanpa perlu mengubah kode
Ketuju, memodifikasi isi variable environment sesuai dengan kredensial database saya dan juga memodifikasi Allowed_host dan database di settings.py
Kedelapan, Saya membuat deployment melalui PWS dan menambahkan kredensial database di raw editor di PWS dengan SCHEMA tugas_individual dan juga mengedit settings.py untuk menambahkan url website di Allowed_host
Kesembilan, menjalankan PWS untuk Git Kredensial Manajer agar proyek dapat dijalankan melalui PWS

*** Melakukan routing pada proyek agar dapat menjalankan aplikasi main. --- DONE ***
*** Membuat sebuah proyek Django baru --- DONE ***
*** Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. --- DONE ***

Kesepuluh, membuat aplikasi dengan nama main yang akan berisikan struktur awal Django lalu mendaftarkan main ke 
Installed_apps di settings agar dapat mendaftarkan aplikasi main ke dalam proyek.

*** Membuat aplikasi dengan nama main pada proyek tersebut. --- DONE ***

Kesebelas,  membuat direktori templates yang berisi main.html
Keduabelas, mengubah isi models.py dengan nama fungsi Product dan memiliki atribut yang diinginkan beserta category choices yang di inginkan

*** Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib --- DONE ***

Keduabelas, melakukan migrations untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru
Ketigabelas, mengedit file views.py agar memiliki fungsi show_main yang menerima parameter request. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai. Di sini juga memberikan return render berfungsi untuk me-render tampilan main.html
Keempatbelas, mengedit file main.html di templates agar dapat menampilkan data dari model 

***  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. --- DONE ***

Kelimabelas, mengedit file urls.py di direktori main yang berfungsi untuk menghubungkan URL kosong ('') dengan fungsi show_main yang berada di dalam aplikasi bernama main
Keenambelas, mengedit file urls.py di fantasy_shop di bagian urlpatterns untuk menambahkan rute URL untuk mengarahkan ke tampilan main

*** Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. --- DONE ***

Ketujuhbelas, melakukan add, commit, push ke git dan pws

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://miro.medium.com/v2/resize:fit:1400/1*XohhamnRotq53fQaY5HQfA.png
    User: Pengguna adalah client yang memulai interaksi. Ia mengirimkan request (permintaan) melalui browser ke aplikasi Django.

    URL: Setiap request dari pengguna akan diterima oleh sistem URL sebagai dispatcher dari Djanggo, URL ini berfungsi untuk mencocokkan URL yang diminta dengan pola yang telah di definisikan di dalam file urls.py. Setelah dicocokkan, URL akan mengarahkan permintaan ke view yang sesuai

    View: View akan menerima permintaan dari URL. View ini berfungsi untuk memproses permintaan dari URL, permintaan ini mungkin mengharuskan view untuk berinteraksi dengan Model untuk mengambil atau menyimpan data, melakukan perhitungan, atau memvalidasi input dari pengguna. Setelah selesai, view akan memilih template yang tepat untuk menampilkan hasil

    Model: Model merupakan representasi data dari aplikasi. Model berfungsi untuk berinteraksi dengan database dan mengambil data yang diminta oleh view lalu dikirim lagi ke view. Di database, kita akan mendefinisikan struktur data, hubungan antar data, dan cara data tersebut diakses.

    Template: Template berfungsi untuk memperlihat data yang diterima dari view. Template akan menghasilkan halaman HTML akhir yang akan dikirim kembali ke pengguna.

Jelaskan peran settings.py dalam proyek Django!
    settings.py memiliki peran untuk menkontrol bagaimana proyek django bekerja, mulai dari mendaftarkan aplikasi, mengelola url, keamanan, dan lain halnya. Di tugas 2, hal yang di ubah dari settings.py yaitu menambahkan main di INSTALLED_APPS sehingga aplikasi main yang kita buat dapat dimuat aplikasinya, kita juga menambahkan ALLOWED_HOSTS yang berfungsi sebagai nama domain yang dapat memuat aplikasi kita.

Bagaimana cara kerja migrasi database di Django?
    Proses migrasi melibatkan 2 tahap yaitu makemigrations dan migrate. Makemigrations berfungsi untuk membuat file yang berisikan perubahan model yang belum di aplikasikan ke dalam basis data. Tahap kedua yaitu migrate, migrate ini berfungsi untuk mengaplikasihkan perubahan yang ada dalam file yang telah dibuat dari makemigrations. Migrasi merupakan cara Django melacak perubahan pada model basis data.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut Saya, alasan mengapa Djanggo digunakan sebagai permulaan karena Django ini memiliki banyak fitur untuk membangun web sehingga tidak memerlukan waktu yang banyak untuk menelusuri library di internet untuk di import. Django juga memakai pendekatan MVT model yang dapat membantu pemula untuk memahami setiap bagian dari aplikasi web yang terhubung satu sama lain.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Sejauh ini, selama saya mengikuti tutorial 1 dengan tidak banyak kendala dan asisten dosennya cukup aktif dalam membantu dalam menyelesaikan masalah khususnya waktu kemarin ketika tutorial 0 yang saya beberapa kali bermasalah.