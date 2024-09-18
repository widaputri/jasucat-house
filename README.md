## [Jasucat House](http://wida-putri31-jasucathouse.pbp.cs.ui.ac.id/)

# Tugas 2

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
```
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
```
Di blok kode di atas, objek Product melambangkan satu tabel di basis data, sedangkan name, price, description, dan stock melambangkan kolom-kolom di tabel tersebut.


# Tugas 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting dalam pengimplementasian platform karena memastikan komunikasi yang cepat dan aman antara komponen, sehingga data dapat diakses secara real-time, sinkron, dan efisien. Hal ini meningkatkan performa platform, menjaga keamanan informasi, dan memungkinkan platform untuk berskala besar dengan latensi yang rendah. Data delivery yang handal juga memastikan bahwa pengguna selalu bekerja dengan data yang up-to-date, mendukung pertumbuhan platform tanpa mengorbankan kualitas layanan.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih populer dibandingkan XML karena lebih sederhana, ringan, dan mudah dibaca, baik oleh manusia maupun mesin. JSON memiliki sintaks yang lebih ringkas dan langsung dibandingkan XML, yang seringkali memerlukan tag pembuka dan penutup yang memperbesar ukuran data. Selain itu, JSON lebih mudah digunakan dalam pemrograman modern, terutama dalam JavaScript, karena objek JSON secara langsung dapat diparsing menjadi objek JavaScript. Kinerja parsing JSON juga umumnya lebih cepat dibandingkan XML, yang menjadikannya pilihan utama dalam pengiriman data melalui API dan layanan web di era aplikasi berbasis web yang dinamis. Menurut saya, keduanya memiliki kelebihan dan kekurangannya masing-masing, JSON lebih sederhana dan ringan, sementara XML lebih fleksibel dan sering digunakan untuk skenario yang memerlukan format data yang lebih kompleks.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi semua validasi yang telah didefinisikan di dalam form tersebut. Method ini memproses input, memeriksa apakah data sesuai dengan tipe yang diharapkan, dan memastikan semua aturan validasi (seperti panjang maksimum, format, dan keharusan diisi) terpenuhi. Jika semua data valid, is_valid() akan mengembalikan nilai True, dan data yang divalidasi dapat diakses melalui cleaned_data. Method ini penting untuk memastikan bahwa data yang diterima dari pengguna bersih, aman, dan sesuai untuk diproses lebih lanjut oleh aplikasi sebelum disimpan atau digunakan.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token dalam form Django diperlukan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), di mana penyerang dapat mencoba mengirim permintaan berbahaya atas nama pengguna yang sedang terautentikasi di aplikasi tersebut tanpa sepengetahuan mereka. Token ini memastikan bahwa setiap permintaan POST yang diterima server berasal dari sumber yang sah dengan memverifikasi token unik yang dikirim bersama form. Jika tidak ada csrf_token, penyerang dapat memanfaatkan kelemahan ini dengan membuat permintaan berbahaya dari situs lain, misalnya mengirim form tanpa izin pengguna, yang dapat mengakibatkan pencurian data, perubahan data, atau tindakan berbahaya lainnya di aplikasi. Dengan csrf_token, hanya permintaan yang berasal dari sumber yang valid yang akan diproses oleh server, sehingga meningkatkan keamanan aplikasi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat input form untuk menambahkan objek model pada app sebelumnya.
Pengerjaan dimulai dengan mengubah primary key Products menjadi UUID agar lebih aman. Selanjutnya, membuat struktur form baru di forms.py dan mengimportnya ke views.py. lalu, di views.py, membuat fungsi create_product(request). Form harus dipastikan valid dan request methodnya POST. Lalu memodifikasi fungsi show_main agar dapat mendisplay data kita. Terakhir, membuat create_product.html untuk halaman penginputan data dan melakukan routing untuk halaman tersebut.

### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Untuk menampilkan semua data, kita membuat fungsi yang mengambil semua data kita dan mereturn hasil serialisasinya menjadi JSON/XML. Untuk by ID, mirip tetapi kita perlu menambahkan parameter ID serta memfilter datanya by ID.

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Mengimport ke urls.py di main dan menambahkan path yang sesuai.