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
Working on it 👷‍♂️

### 📝 How I Did It
Working on it 👷‍♂️
- [x] Task 1
- [x] Task 2
- [x] Task 3



## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
