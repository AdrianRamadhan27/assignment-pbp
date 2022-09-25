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
Working on it 👷‍♂️

### 📊 Data Flow
Working on it 👷‍♂️

### 📝 How I Did It
Working on it 👷‍♂️
- [x] Task 1
- [x] Task 2
- [x] Task 3



## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
