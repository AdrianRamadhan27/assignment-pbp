# Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Raden Mohamad Adrian Ramadhan Hendar Wibawa - 2106750540

## Tugas 3 - MyWatchlist

### 🌐 Deployed App 

[My Watchlist App](https://pbp-assignment-2106750540.herokuapp.com/mywatchlist/html/)

### 📙 HTML, XML, and JSON
- **HTML** adalah HyperText Markup Language yang biasanya digunakan untuk pengembangan tampilan website. 
- **XML** adalah eXtensible Markup Language yang biasanya digunakan untuk menyimpan, mengirim, dan merekonstruksi data arbitrary.
- **JSON** adalah JavaScript Object Notation yang biasanya digunakan untuk merepesentasikan data dan transmitnya pada website.


Perbedaan dari ketiganya ini adalah sebagai berikut


| HTML | XML | JSON |
|------|-----|------|
| Merupakan bahasa markup | Merupakan bahasa markup dan format file | Merupakan format data-interchange |
| Difokuskan pada presentasi | Difokuskan pada transfer data | Difokuskan pada transfer data |
| Mengutamakan format | Mengutamakan konten/data | Mengutamakan konten/data |
| Tagnya predefined dan terbatas | Tagnya tidak predefined tetapi extensible | Tidak menggunakan tag |
| Tidak menyediakan namespace | Menyediakan namespace | Tidak menyediakan namespace |

### 🚚 Data Delivery
Ketika kita ingin mengimplementasikan suatu platform, kita tidak bisa hanya menggunakan data *static* atau template karena akan menjadi percuma. Kita memerlukan data asli *real-time* yang disimpan dalam database dan perlu kita tampilkan ketika seorang user memanggil request. Untuk itu, data yang tersimpan itu perlu adanya sistem untuk mengirim data dari satu tampilan ke tampilan lainnya. Dengan data delivery inilah user dapat menerima data secara langsung. Data delivery dapat keluar dalam bentuk API layaknya JSON setelah suatu proses back-end, yang kemudian dapat dimasukkan ke template front-end layaknya HTML. 

### 📝 How I Did It
- [x] Membuat suatu aplikasi baru bernama `mywatchlist` di proyek Django Tugas 2 pekan lalu
Untuk membuat app baru, aku pertama membuka terminal di root folder dari django_project dan menjalankan `python manage.py startapp mywatchlist`. Setelah itu akan muncul folder baru bernama `mywatchlist` yang digunakan untuk pengembangan aplikasi mywatchlist.

- [x] Menambahkan path `mywatchlist` sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
Untuk menambah path ke app baru, aku pertama membuat file `urls.py` di folder mywatchlist dan mengisinya dengan array urlpatterns (untuk sementara kosongkan dulu). Setelah itu, aku buka folder `project_django` dan pada file `urls.py` nya kutambahkan path baru di dalam urlpatterns. Path yang dibuat adalah `path('/mywatchlist', include('mywatchlist.urls'))`. Tak lupa, aku juga menambahkan 'mywatchlist' pada array **INSTALLED_APPS** di dalam `settings.py`.

- [x] Membuat sebuah model `MyWatchList`
Sesuai dengan kriteria atribut di soal, pada file `models.py` aku membuat class baru bernama `MyWatchlist` dengan sebagai berikut.
  - [x] `watched` bertipe BooleanField
  - [x] `title` bertipe CharField
  - [x] `rating` bertipe IntegerField (dengan validator `MinValueValidator(1)` & `MaxValueValidator(5)`)
  - [x] `release_date` bertipe DateField
  - [x] `review` bertipe TextField 

### 👮 Postman Request Results
- ![HTML Request](https://github.com/AdrianRamadhan27/assignment-pbp/blob/main/static/images/postman-mywatchlist-html.jpg)
*Accesing https://pbp-assignment-2106750540.herokuapp.com/mywatchlist/html/*


- ![XML Request](https://github.com/AdrianRamadhan27/assignment-pbp/blob/main/static/images/postman-mywatchlist-xml.jpg)
*Accesing https://pbp-assignment-2106750540.herokuapp.com/mywatchlist/xml/*


- ![JSON Request](https://github.com/AdrianRamadhan27/assignment-pbp/blob/main/static/images/postman-mywatchlist-json.jpg)
*Accesing https://pbp-assignment-2106750540.herokuapp.com/mywatchlist/json/*


### Testing
Aku telah mengimplementasikan 3 url di `mywatchlist`. Untuk menjalankannya, hanya perlu run `python manage.py test mywatchlist`tapi pastikan sudah menjalankan `python manage.py collectstatic` sebelumnya. Test ini akan mengecek `status_code` dari response yang diberikan setiap url dan hanya akan bisa lulus tes jika mengembalikan `200 OK`.


## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
