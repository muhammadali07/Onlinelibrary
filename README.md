# Onlinelibrary

# Langkah menjalankan aplikasi/service Back End
1. cloning repo 
2. pindah ke direktori be
3. copy file sample.env menjadi .env
4. jalankan perintah untuk build container : docker-compose up -d --build
5. tunggu hingga proses selesai
6. setelah ter-build,..Buat konfigurasi konek ke database menggunakan aplikasi database client semisal : DBeaver:
  - username  : grit_user
  - password : grit_password
  - port : 5439
  - test connection
8. setelah sukses terkoneksi: buat database dengan nama : grit_development
9. kemudian restart service be dengan perintah : docker-compose restart api
10. kemudian buka browser dan akses http://localhost:8888/api/docs untuk testing API
11. untuk testing API bisa menggunakan OpenAPI Swagger yang sudah di sediakan atau bisa juga via Postman


# step testing API
1. buat user account terlebbih dahulu agar bisa akses mendapatkan token jwt pada API http://localhost:8888/api/v1/users/create-new-users
2. login pada endpoint http://localhost:8888/api/v1/access/login untuk mendapatkan Token Bearer
3. Silahkan testing API.
4. Terima Kasih
