# Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Raden Mohamad Adrian Ramadhan Hendar Wibawa - 2106750540

## Tugas 1 - Platform Essay
[Platform: What is it?](https://drive.google.com/file/d/10xfIkMP9gC5HLdUUkkHPvTSbV1zxJWBr/view?usp=sharing)

## Tugas 2 - Katalog

### Deployed App
[Catalog App](https://pbp-assignment-2106750540.herokuapp.com/katalog/)

### Django Scheme
![Bagan Django](https://github.com/AdrianRamadhan27/assignment-pbp/blob/main/assignment1_chart.gif)


*Made with [Canva](https://www.canva.com)*

Pada framework **Django**, kita dapat membuat suatu aplikasi yang mengimplementasikan struktur **MVT** (Model, View, Template). Model di sini merepresentasikan *entity* pada database (dipelahari di Basis Data). Views bisa dibilang adalah tempat algoritma yang melakukan proses atas *request* dan *response* sehingga aplikasi bisa berjalan. Template adalah tampilan (*front-end*) yang akan dilihat oleh pengguna.

Ketika seorang user membuat request untuk aplikasi ini, `urls.py` pada folder `project_django` akan melakukan *routing* berdasarkan jenis url request yang diterima. Setelah itu, ia akan memanggil aplikasi yang ada, salah satunya adalah **katalog**. Dalam folder katalog, juga ada `urls.py` yang mengatur routing untuk url dengan prefix `katalog/`. Jika tidak ada prefix tambahan, yang akan dipanggil adalah function `show_katalog()` dari `views.py`. Function ini akan memanggil data bermodelkan `CatalogItem` yang terdefinisikan pada `models.py` dari database yang masih berupa file `.json`. Setelah itu, function ini juga akan me-*render* file template `katalog.html` dengan konteks berupa data tadi. Baru lah user akan ditampilkan aplikasi katalog dengan tabel data yang ada. 

### Usage of Virtual Environment
Dalam pengembangan aplikasi Django di repositori lokal komputer kita, dibutuhkan sebuah Virtual Environment yang dapat kita buat dengan command `python -m venv [nama_environment]`. Command ini akan membuat folder dengan nama environment yang kita pilih dan kita dapat mengaktifkan Virtual Environment dengan `/Scripts/activate.bat` di dalam folder ini. Berdasarkan [Andrade](https://towardsdatascience.com/why-you-need-a-python-virtual-environment-and-how-to-set-it-up-35019841697d), Virtual Environment ini digunakan agar kita tidak perlu menyesuaikan *requirements*/*dependencies* yang dibutuhkan project di komputer kita secara global. Kita hanya perlu meng-*install* nya di virtual environment dan project kita bisa dijalankan. 

### How I Did It
Dari template project yang sudah disediakan, aku ditugaskan untuk:
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
Aku membuat sebuah fungsi `show_katalog()` yang mengambil data dengan memanggil `CatalogItem.objects.all()` yang berisi data yang dibuat dari command `python manage.py loaddata inital_catalog_data.json`. Aku lalu membuat sebuah dictionary `context` yang isinya adalah data yang akan ditampilkan pada file HTML. Nama data beserta value yang ada diantaranya adalah nama, npm, dan list_catalog. Setelah itu aku me-`return` pemanggilan function `render` dengan parameter pertama adalah request, parameter kedua adalah file `katalog.html`, dan parameter ketiga adalah `context`. Oiya, file `index.html` di dalam `/katalog/templates/` kuganti namanya agar tidak berkomplikasi dengan file dengan nama yang sama di `example_app`.   
2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
Untuk membuat sebuah routing, aku pertama-tama membuat file `urls.py` di dalam folder katalog. Di dalamnya ada sebuah array `urlpatterns`  
3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
