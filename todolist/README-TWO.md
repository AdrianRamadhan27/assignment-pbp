# Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Raden Mohamad Adrian Ramadhan Hendar Wibawa - 2106750540

## Tugas 6 - Javascript and AJAX

### 🌐 Deployed App 

[To Do List App](https://pbp-assignment-2106750540.herokuapp.com/todolist/)


### 🔄 Asynchronous vs Synchronous Programming
- **Asynchronous** Programming adalah teknik yang memungkinkan program untuk memulai task yang berpotensi berjalan lama dan masih dapat responsif terhadap event lain saat task itu berjalan, sehingga tidak perlu menunggu task tersebut usai. 

- **Synchronous** Programming adalah model pemrograman di mana task berlangsung secara berurutan. Dalam model ini, operasi terjadi satu demi satu. Program pindah ke task berikutnya ketika task saat ini telah menyelesaikan eksekusi dan telah mengembalikan hasil.

| Asynchronous | Synchronous |
| ------------ | ----------- |
| Multi-thread, operasi pada program berjalan secara paralel | Single-thread, hanya satu operasi yang berjalan tiap waktu |
| Non-blocking, dapat mengirimkan lebih dari 1 request ke server | Blocking, hanya dapat mengirimkan satu request dan harus menunggu response |
| Lebih cepat | Lebih lambat dan metodikal |
 
### 🖱 Event-Driven Programming
Event-Driven Programming adalah paradigma di mana entitas (objek, layanan, dan sebagainya) berkomunikasi secara tidak langsung dengan mengirimkan pesan satu sama lain melalui perantara. Pesan biasanya disimpan dalam sebuah queue sebelum dijalankan.
Event adalah potongan data yang dikirim oleh user dan akhirnya diterima oleh program. Salah satu contohnya adalah sebagai berikut.

```Javascript
$("#close-modal").click(function() {
   $("#my-modal").attr("style", "display:none");
});
```
Pada blok kode di atas, script akan mengubah atribut dari tag HTML dengan id `my-modal` setelah button `close-modal` di-_click_. Click ini lah yang merupakan salah satu contoh dari event.

### 🔃 Asynchronous Programming in AJAX
Jelaskan penerapan asynchronous programming pada AJAX.
AJAX adalah singkatan dari Asynchronous Javascript And XML. Ini adalah teknik yang digunakan mengirim dan mengambil data dari server. Proses ini dilakukan secara asinkron agar tidak mengganggu keadaan halaman web saat ini. AJAX mencakup bidang teknologi web development yang saling berinteraksi satu sama lain. Ini termasuk HTML (XHTML), CSS, DOM, JSON (XML), dan Javascript.
Berikut adalah cara kerja AJAX. \
![image](https://user-images.githubusercontent.com/58902925/194973930-83735b0e-133f-4b74-991e-561e3f011a39.png) \
_https://www.w3schools.com/_
1. Sebuah event terjadi pada halaman web
2. Object `XMLHttpRequest` dibuat oleh JavaScript
3. Object `XMLHttpRequest` mengirimkan request ke server
4. Server memproses request tersebut
5. Server mengembalikan response ke halaman web
6. Response tersebut dibaca oleh JavaScript
7. Sebuah _action_ dilakukan oleh JavaScript

### 📝 How I did it
- [x] Mengubah tugas 4 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
  - [x] AJAX GET
    - [x] Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
    - [x] Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
    - [x] Lakukan pengambilan task menggunakan AJAX GET.
  - [x] AJAX POST
    - [x] Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
    - [x] Buatlah view baru untuk menambahkan task baru ke dalam database.
    - [x] Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
    - [x] Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
    - [x] Tutup modal setelah penambahan task telah berhasil dilakukan.
    - [x] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.


## Thank You
P.S. Capekan nulis README.md nya daripada bikin appnya 🤭.

