# Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Raden Mohamad Adrian Ramadhan Hendar Wibawa - 2106750540

## Tugas 4 - ToDoList

### 🌐 Deployed App 

[To Do List App](https://pbp-assignment-2106750540.herokuapp.com/todolist/)

### 💽 csrf_token
CSRF atau Cross Site Request Forgery dapat terjadi ketika suatu situs yang _malicious_ menyebabkan browser pengguna membuat request ke server yang menyebabkan suatu perubahan pada server. Server akan mengira bahwa request yang dibuat merupakan niatan dari pengguna karena memiliki _credentials_ pengguna yaitu cookies.
Dengan menambahkan tag `csrf_token` ke dalam tag `<form>` di dalam template project django, kita dapat memastikan bahwa request-request yang tergolong 'unsafe' seperti **POST**, **PUT**, dan **DELETE** dapat terlindungi dari adanya CSRF.

### 📋 Making Forms Manually
Jika kita tidak ingin menggunakan `ModelForm` dari `django.forms`, kita dapat membuat form secara manual. Untuk tag yang digunakan pada template masih sama, yaitu tag `<form>` yang di dalamnya kita masukkan juga `{% csrf_token %}`. Nah, yang membedakan adalah pada isi form, kita akan membuat widgets nya secara manual dengan menggunakan tag `<input>` dan sebagainya. Pada tiap widgets ini kita akan berikan attribute `name` yang nantinya akan digunakan untuk mengidentifikasikan jenis atribut model yang dimasukkan. Contohnya  sebagai berikut untuk form create-task.

```html
<form method="POST" action="">
        {% csrf_token %}
        <label for="title">Title</label>
        <input type="text" id="title" name="title"/>
        
        <label for="description">Description</label>
        <textarea id="description" name="description"></textarea>

        <input type="submit", value="Create">
</form>
```

Lalu, pada file `views.py`, function untuk method POST perlu diubah juga. Pertama, kode untuk method get atau yang hanya menampilkan template form nya perlu dipisah dari kode yang memproses form nya. Sehingga kita buat if-statement yang mengecek apakah `request.method` adalah `"POST"`. Lalu di dalam blok if-statement ini, kita buat instance model baru berdasarkan atribut yang dimasukkan dalam form. Kita dapat mengidentifikasi jenis atributnya dengan menggunakan `request.POST.get(name)`. Setelah itu, kita save instance modelnya dan redirect ke halaman yang ditujukan. Contohnya sebagai berikut untuk create-task.
```python
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description, user=request.user)
        task.save()
        return redirect('todolist:show_todolist')

    context = {}
    return render(request, 'create_task.html', context)
```

### 📊 Data Flow
Alur data yang terjadi ketika pengguna menambahkan data adalah bagian dari CRUD (Create, Retrieve, Update, Delete). Ketika pengguna mengisi form di template HTML, data tiap atribut akan disimpan dan dioper ke function di `views.py`. Setelah itu, akan dibuat (create) instance dari model baru berdasarkan atribut yang tersimpan. Kemudian, instance model ini akan disimpan pada database. Terakhir, tiap instance yang ada pada di database akan diambil (retrieve) dengan query khusus agar tampil di template HTML.

### 📝 How I Did It
Berikut adalah caraku mengimplementasikan daftar tugas yang perlu dilakukan
- [x] Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya. \
Sama seperti tugas pekan sebelumnya, jalankan `python manage.py startapp todolist` di terminal proyek django. 
- [x] Menambahkan path `todolist` sehingga pengguna dapat mengakses http://localhost:8000/todolist. \
Tambahkan `'todolist'` ke INSTALLED_APPS di `settings.py`, dan tambahkan `path('/todolist')` ke urlspattern di `urls.py`. Jangan lupa untuk membuat `urls.py` di dalam folder todolist yang berisi array urlpatterns.
- [x] Membuat sebuah model `Task` yang memiliki atribut sebagai berikut: \
        - `user` menggunakan ForeignKey() dengan parameter `django.contrib.auth.models.User` \
        - `date` menggunakan DateField() dengan parameter auto_now_add = `True` agar otomatis ditambahkan ketika Task dibuat \
        - `title` menggunakan CharField() \
        - `description` menggunakan TextField() \
        - Aku juga menambahkan atribut `id` menggunakan AutoField() sebagai primary key dan `is_finished` menggunakan BooleanField() \
        
- [x] Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik. \
1. Untuk registrasi, buat function `register()` pada `views.py`. Tambahkan form ke context template yang akan di render. Form yang digunakan adalah `UserCreationForm()` dari `django.contrib.auth.forms`. Buat template `register.html` yang berisi tag `<form>`. Di dalam tag form jangan lupa sertakan `csrf_token`. Terakhir, tambahkan `{{ form.as_table }}` untuk memanggil form user yang ada di function dalam bentuk tabel.
2. Halaman login akan menjadi halaman paling awal yang bisa diakses pengguna. Buat terlebih dahulu template `login.html` yang berisi form login. Form login berisi input title dan input description yang pada tag nya terdapat atribut `name` yang akan digunakan pada function di `views.py`. Function `login_user()` yang dibuat akan mengambil data username dan password dari `request.POST` lalu dengan function authenticate akan dicek apakah terdapat user yang cocok di database. Tambahkan cookies agar data user setelah login disimpan oleh server. Baru setelah itu redirect ke halaman utama todolist.
3. Tambahkan function `logout_user()` Function ini akan memanggil function logout(request) dan menghapus cookies yang telah dibuat setelah login. Simpelnya, function ini melakukan opposite dari login_user().

- [x] Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task. \
Buat function `show_todolist()` yang memiliki context berisi username yang berasal dari cookies dan data Task yang telah dibuat oleh user saat ini. Gunakan method `objects.filter()` untuk me-*retrieve* Task yang memenuhi `user = request.user`. Pada template `todolist.html`, Panggil username context untuk menampilkan pengguna saat ini. Buat tabel yang isi `<tbody>` nya adalah for loop untuk setiap task yang diterima dari context. Tambahkan tombol `logout` di bawah tabel tersebut. Agar pengguna tidak dapat mengakses halaman todolist tanpa login, tambahkan `@login_required(login_url='/todolist/login')` di atas pendefinisian function `show_todolist()`.
- [x] Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task. \
Buat file baru bernama `forms.py` didalam folder todolist. Pada file ini, buat sebuah class bernama TaskForm yang meng-*extend* class `ModelForm` dari django.forms. Di dalam definisi class ini, buat class Meta dengan 2 atribut. Atribut pertama adalah model yang menyimpan model Task. Atribut satunya lagi adalah fields yang merupakan array berisi field yang dapat diisi user pada form saat pembuatan Task. Pada kasus ini, fields yang perlu diisi hanyalah `title` dan `description`. 
Setelah itu, buat function `create_task()` di `views.py`. Implementasi function ini kurang lebih sama dengan function `register()` hanya saja setelah membuat object task, assign attribute user menjadi request.user lalu save lagi objek task agar disimpan pada database.
Pada template `create_task.html` tidak perlu banyak yang perlu diubah jika menyalin dari template `register.html`. Modifikasi sesuka hati agar lebih relevan dengan fungsi halamannya.
- [x] Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:
 - http://localhost:8000/todolist berisi halaman utama yang memuat tabel task. 
 Tambahkan path('') pada urlpatterns yang memanggil function `show_todolist()`.
 - http://localhost:8000/todolist/login berisi form login.
 Tambahkan path('login/') pada urlpatterns yang memanggil function `login_user()`
 - http://localhost:8000/todolist/register berisi form registrasi akun.
 Tambahkan path('register/') pada urlpatterns yang memanggil function `register()`
 - http://localhost:8000/todolist/create-task berisi form pembuatan task.
 Tambahkan path('create-task/') pada urlpatterns yang memanggil function `create_task()`
 - http://localhost:8000/todolist/logout berisi mekanisme logout.
 Tambahkan path('logout/') pada urlpatterns yang memanggil function `logout_user()`
- [x] Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. \
Karena aplikasi dari tugas 2 sudah dideploy menggunakan repository yang sama, yang perlu dilakukan hanyalah commit perubahan ke repository github.
- [x] Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
Tambahkan User baru dengan membuka aplikasi yang telah di deploy dengan 2 cara. Cara pertama adalah memanfaatkan fitur admin django. Agar bisa login ke situs admin. Jalankan `python manage.py createsuperuser` di terminal aplikasi heroku dan buat sebuah akun admin. Masuklah ke halaman admin dan tambahkan user baru di database User.
User baru juga bisa dibuat dengan mendaftarkan akun pada halaman register yang telah dibuat. Setelah itu, buat 3 task dengan form create-task pada masing-masing akun. Mirisnya, jumlah tugas pekan ini lebih dari 6 :(.

## Thank You
P.S. Capekan nulis README.md nya daripada bikin appnya 🤭.

