# Tugas 2
## [Jasucat House](http://wida-putri31-jasucathouse.pbp.cs.ui.ac.id/)

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat sebuah proyek Django baru.
Langkah pertama adalah membuat virtual environment agar dependencies aplikasi tidak nabrak dengan yang sudah diinstall, lalu menginstall semua dependency yang akan diperlukan aplikasi. Lalu, inisiasi proyek Djangonya. Jangan lupa untuk configure allowed hosts agar dapat dijalankan. Jangan lupa juga dihubungkan ke GitHub

### Membuat aplikasi dengan nama main pada proyek tersebut.
Start app main dan tambah ke installed apps.

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Menambahkan urls main ke urls jasucat_house untuk menghubungkan dengan rute URL proyek

### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
Dibuat di models.py sesuai keperluan. Menambah atribut stock juga.

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Buat context di views dan pastikan cocok dengan template variables sesuai. Render di views.py

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Membuat urls.py di main dan menampilkan show_main.

### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Jalankan project command yang muncul setelah memulai proyek baru di PWS dan push ke PWS tiap ada perubahan.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan](bagan_tugas2.png)

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Melacak perubahan kode dan menyimpan versi-versi sebelumnya agar ketika menemukan masalah dapat dipulihkan kembali ke versi tanpa error. Juga mendukung kolaborasi tim agar kode semua developer dapat terintregrasi dengan baik.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django berbasis python yang jika dibandingkan dengan bahasa pemrograman lain terhitung cukup intuitif bagi pemula. Merupakan bahasa yang populer juga sehingga dokumentasi lengkap dan mudah untuk troubleshooting dari komunitas.

## Mengapa model pada Django disebut sebagai ORM?
ORM adalah teknik pemrograman yang digunakan untuk berinteraksi dengan basis data lewat pemetaan objek dalam suatu bahasa pemrograman ke tabel dalam basis data relasional. Misal:
'''
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
''''
Di blok kode di atas, objek Product melambangkan satu tabel di basis data, sedangkan name, price, description, dan stock melambangkan kolom-kolom di tabel tersebut.