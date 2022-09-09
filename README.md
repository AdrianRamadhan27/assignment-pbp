# Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023
Oleh Raden Mohamad Adrian Ramadhan Hendar Wibawa - 2106750540

## Link to App
[Catalog App](https://pbp-assignment-2106750540.herokuapp.com/katalog/)

## Bagan
![Bagan Django](https://github.com/AdrianRamadhan27/assignment-pbp/blob/main/assignment1_chart.gif)

Django merupakan framework yang mengikuti struktur MVT (Model-View-Template). MVT adalah salah satu turunan dari struktur MVC (Model-View-Controller), namun model-nya lebih difokuskan sebagai objek yang mendefinisikan entitas pada database beserta konfigurasinya, lalu views berperan sebagai logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk, dan template berperan sebagai tampilan yang akan dikembalikan kepada pengguna.

Adapun alur sebuah permintaan diproses di Django adalah sebagai berikut. Pertama, permintaan yang masuk ke dalam server Django akan diproses melalui urls untuk diteruskan ke views yang didefinisikan oleh pengembang untuk memproses permintaan tersebut. Apabila terdapat proses yang membutuhkan keterlibatan database, maka nantinya views akan memanggil query ke models dan database akan mengembalikan hasil dari query tersebut ke views. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut dikembalikan ke pengguna sebagai respons.

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
