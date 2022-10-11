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
    
    Aku membuat function `show_json()` yang mengembalikan object `HttpResponse`tipe json.
    - [x] Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
    
    Aku tambahkan path('json/') ke `urls.py` yang memanggil function `show_json()`
    - [x] Lakukan pengambilan task menggunakan AJAX GET.
    
    Pertama aku ubah function `show_todolist()` untuk tidak perlu retrieve semua object task. Lalu pada template `todolist.html` aku tambahkan script jQuery yang dibungkus `$(document).ready(function{})` agar script langsung jalan saat halaman di-load. Script yang digunakan adalah `$getJSON()` untuk menerima json dari `todolist/json/` dan `$each()` yang melakukan iterasi untuk tiap object task pada database. Pada tiap iterasi, aku menambahkan tag HTML yang sebelumnya sudah ada secara synchronous programming. Berikut adalah potongan kode yang dimaksud.
```Javascript
$(document).ready(function(){
   $.getJSON("{% url 'todolist:show_json' %}", function(data) {
       var grid = [];
       $.each(data, function(index, value) {
           var cards = [];
           var content = [];
           var status = ""
           if ((value.fields.is_finished)){
               status = "Selesai";
           } else {
               status = "Belum Selesai"
           }
           . . .
```
  - [x] AJAX POST
    - [x] Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.

    Tombol yang sudah kubuat di Tugas 4 dan Tugas 5 aku gunakan kembali, hanya saja tombol ini tidak mengarah ke halaman create-task. Aku membuat sebuah modal menggunakan tailwind-CSS yang aku ikuti dari tutorial berikut: [Creating a Modal Dialog With Tailwind CSS](https://www.section.io/engineering-education/creating-a-modal-dialog-with-tailwind-css/). Aku atur style display nya menjadi none untuk default. Dengan jQuery aku buat jika tombol ditekan display nya menjadi block. Pada modal ini kubuat form secara manual.
    - [x] Buatlah view baru untuk menambahkan task baru ke dalam database
    
    Aku membuat function `add_task_ajax()` yang akan membuat object Task dari form add task modal jika method dari request adalah POST. Setelah itu, function ini akan mengembalikan response dalam bentuk Json sebagai status keberhasilan data yang ditambahkan.
    - [x] Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
    
    Aku tambahkan path(`add/`) ke urls.py.
    - [x] Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
    
    Ketika form task di-_submit_, Jquery akan memanggil request ajax dengan method post ke url todolist/add yang sebelumnya ditambahkan. Berikut kode yang dimaksud.
    
```Javascript
$("#task-form").submit(function(e){
    e.preventDefault();
    $("#add-btn").prop('disabled', true);
    $("#add-btn").text('Processing...');
    var $form = $(this);
    var serializedData = $form.serialize();
    $.ajax({
        url: "{% url 'todolist:add_task' %}",
        type: "POST",
        data: serializedData,
        dataType: 'json',
        success: function (data) {
        . . . 
```

   - [x] Tutup modal setelah penambahan task telah berhasil dilakukan.
   
   Selain menambahkan data task, submit form juga akan mengembalikan style dari modal menjadi display:none.
   
```Javascript
$("#my-modal").attr("style", "display:none");
```
   - [x] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
   
   Agar halaman dapat te-_refresh_ secara asinkronus tanpa reload seluruh page. Aku ulangi proses getJSON dari method GET setelah sebuah form disubmit.

## Thank You
P.S. Capekan nulis README.md nya daripada bikin appnya 🤭.

