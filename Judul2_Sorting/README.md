#  Pengurutan Nama Mahasiswa berdasarkan NPM (Insertion Sort)

## a. Judul Program
Pengurutan Nama Mahasiswa berdasarkan NPM menggunakan Insertion Sort

## b. Deskripsi Singkat
Program ini dirancang untuk mengelola dan mengurutkan data mahasiswa berdasarkan Nomor Pokok Mahasiswa (NPM) dengan memanfaatkan algoritma pengurutan Insertion Sort. Melalui antarmuka menu, pengguna dapat menambahkan data mahasiswa baru yang berisi nama dan NPM, serta menampilkan keseluruhan daftar mahasiswa yang telah terurut secara rapi. Sistem ini beroperasi dengan cara membandingkan nilai NPM dari elemen data yang sedang diproses dengan elemen-elemen sebelumnya, kemudian menyisipkannya pada posisi yang tepat sehingga seluruh daftar mahasiswa pada akhirnya tersusun secara ascending (dari nilai terkecil ke terbesar). Selain itu, program ini juga mengimplementasikan exception handling menggunakan blok try-except untuk menangani error dan memberikan peringatan apabila pengguna memasukkan format input yang tidak valid, seperti menginputkan huruf pada pilihan menu atau pada data NPM yang seharusnya berupa angka.

## c. Source Code
berikut adalah kode dari program Pengurutan Nama Mahasiswa berdasarkan NPM menggunakan Insertion Sort
<img width="828" height="731" alt="image" src="https://github.com/user-attachments/assets/1e0835d0-a0a2-4319-a60c-070f3bfeece4" />
<img width="769" height="302" alt="image" src="https://github.com/user-attachments/assets/2faab78d-b6f6-4229-94e0-aceb5e2ddc1e" />


###  Penjelasan Kode
1. Fungsi insertion_sort(students)

- Digunakan untuk mengurutkan daftar data mahasiswa berdasarkan atribut NPM (Nomor Pokok Mahasiswa) dari nilai terkecil hingga terbesar (ascending) menggunakan algoritma Insertion Sort.
- n = len(students) → Menyimpan jumlah elemen data mahasiswa yang ada di dalam list.
- Melakukan perulangan for i in range(1, n) yang dimulai dari elemen kedua (indeks ke-1) hingga akhir, dengan asumsi elemen pertama (indeks ke-0) sudah berada di posisi yang benar.
- temp_student = students[i] → Menyimpan data mahasiswa (berisi nama dan NPM) yang sedang dievaluasi posisinya ke dalam variabel sementara.
- j = i - 1 → Mendeklarasikan indeks penunjuk untuk elemen yang berada tepat di sebelah kiri elemen yang sedang dievaluasi.
- Perulangan while j >= 0 and students[j]['npm'] > temp_student['npm']: digunakan untuk membandingkan NPM elemen sebelumnya dengan NPM yang ada di variabel sementara. Jika NPM sebelumnya lebih besar, maka:
- students[j + 1] = students[j] → Menggeser elemen yang lebih besar tersebut satu posisi ke kanan.
- j -= 1 → Mengurangi nilai penunjuk indeks j untuk mengecek elemen di sebelah kirinya lagi.
- students[j + 1] = temp_student → Menyisipkan data mahasiswa dari variabel sementara ke posisi yang sudah tepat di antara elemen-elemen yang sudah terurut.

2. Fungsi main()

- Bertugas sebagai program utama untuk mengelola interaksi dengan pengguna (input/output) dan mengeksekusi logika pengurutan.
- Input Jumlah Mahasiswa:
- Meminta pengguna memasukkan jumlah mahasiswa.
- Menggunakan blok try-except ValueError untuk memastikan input jumlah mahasiswa adalah angka (integer). Jika input tidak valid (misalnya huruf), program mencetak peringatan "Input tidak valid!" dan berhenti eksekusi.
- Input Data Mahasiswa (Nama & NPM):
- Membuat list kosong students = [] untuk menampung data.
- Melakukan perulangan for sebanyak jumlah mahasiswa yang diinputkan.
- Di dalam perulangan tersebut, terdapat Nested Loop while True yang diiringi blok try-except khusus untuk input NPM. Tujuannya adalah untuk memaksa pengguna memasukkan format angka pada NPM. Jika pengguna salah memasukkan format, program akan mencetak "Input NPM tidak valid, silakan masukkan angka!" dan terus mengulang permintaan input hingga benar tanpa membuat program mengalami crash.
- Data yang sudah divalidasi akan dimasukkan ke dalam list students menggunakan metode .append() dengan format dictionary {'nama': name, 'npm': npm}.

3. Proses & Output:

- Menampilkan daftar mahasiswa sebelum diurutkan.
- Memanggil fungsi insertion_sort(students) untuk memproses pengurutan data di dalam memori secara in-place.
- Menelusuri hasil akhir dari list menggunakan perulangan for dan mencetak daftar nama beserta NPM mahasiswa yang kini telah berhasil terurut.

## d. Output Program

<img width="374" height="436" alt="image" src="https://github.com/user-attachments/assets/83b6cf5b-fd0a-4e60-b338-910d05d3ee33" />
<img width="1297" height="182" alt="image" src="https://github.com/user-attachments/assets/4c45fb0e-5525-4397-a249-b90c9770c6ae" />

1. Input Jumlah Mahasiswa

- Saat user memasukkan angka dengan benar, program akan langsung berlanjut ke proses pengisian data.
- Kalau user memasukkan huruf atau karakter lain selain angka, program akan memunculkan pesan "Input tidak valid!" dan langsung berhenti saat itu juga.

2. Input Data Mahasiswa (Nama dan NPM)

- Jika user mengisi nama dan mengetikkan NPM menggunakan angka, data tersebut otomatis tersimpan ke dalam memori.
- jika user salah format (misalnya mengisi NPM pakai huruf), akan muncul pesan "Input NPM tidak valid, silakan masukkan angka!". Program tidak akan crash atau berhenti, tapi akan terus meminta user menginputkan NPM sampai format angkanya benar.

3. Tampilan Data Awal

- Setelah semua data selesai dimasukkan, program memunculkan teks "Data Mahasiswa yang diinput:".
- Di sini, user bisa melihat sekumpulan data mentah yang posisinya masih acak, sesuai dengan urutan saat user mengetikkannya tadi.

4. Tampilan Hasil Pengurutan (Insertion Sort)

- Setelah data selesai diurutkan oleh sistem, akan muncul teks "Urutan Mahasiswa berdasarkan NPM (Insertion Sort):".
- Pada bagian akhir ini, program menampilkan daftar lengkap mahasiswa dari NPM terkecil sampai terbesar (ascending).
  
## e. Link Youtube
https://youtu.be/uFuDW9FRHIE
