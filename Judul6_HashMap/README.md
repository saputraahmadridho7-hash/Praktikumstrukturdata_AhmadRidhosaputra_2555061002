#  Manajemen Nilai Raport Siswa 

## a. Judul Program
Manajemen Nilai Raport Siswa Menggunakan Hash Map

## b. Deskripsi Singkat
Program ini dirancang untuk menyimulasikan sistem manajemen data nilai raport siswa secara efisien menggunakan struktur data Hash Map. Sistem ini menggunakan teknik penyelesaian tabrakan (collision resolution) berupa Open Addressing dengan metode Linear Probing. Dalam operasionalnya, program menggunakan nama siswa sebagai kunci (key) yang akan diproses oleh fungsi hash untuk menentukan indeks penyisipan total nilai raport (value) ke dalam tabel berukuran tetap.

Penggunaan metode Linear Probing memastikan bahwa jika terjadi tabrakan (indeks sudah terisi oleh data lain), program akan secara berurutan mencari slot kosong berikutnya di dalam tabel. Untuk menjaga efisiensi ruang dan pencarian, program ini menerapkan manajemen status slot cerdas yang terdiri dari status EMPTY (kosong), OCCUPIED (terisi), dan DELETED (dihapus). Status DELETED berfungsi sebagai penanda (tombstone) agar proses pencarian tidak berhenti prematur dan memungkinkan slot tersebut didaur ulang untuk penyisipan data baru.

Program ini dilengkapi dengan fitur utama untuk menambah atau memperbarui nilai, mencari nilai berdasarkan nama, menghapus data, serta menampilkan seluruh isi struktur Hash Map beserta status tiap slotnya. Di samping itu, program juga mengimplementasikan mekanisme exception handling menggunakan blok try-except pada saat menerima masukan nilai raport untuk menangani potensi error (seperti ValueError), sehingga program tetap berjalan stabil dan mencegah crash saat pengguna tidak sengaja memasukkan tipe data huruf alih-alih angka.

## c. Source Code
berikut adalah kode dari program MMembuat Manajemen Buku Perpustakaan Menggunakan Binary Search Tree
<img width="1286" height="887" alt="image" src="https://github.com/user-attachments/assets/74e4ef71-c1b8-4d1e-b677-d59c15c98f2c" />
<img width="1080" height="807" alt="image" src="https://github.com/user-attachments/assets/e552b534-8c24-48b9-bdfe-d575535f2fb1" />
<img width="1160" height="859" alt="image" src="https://github.com/user-attachments/assets/e17a437b-94a2-4a0f-a44d-b56109dd8b8b" />
<img width="901" height="608" alt="image" src="https://github.com/user-attachments/assets/0bc332ea-55e0-4ef1-8b59-c41d82bb6387" />



###  Penjelasan Kode
1. Class SlotState (Digunakan sebagai enumerasi sederhana untuk merepresentasikan status dari setiap slot di dalam Hash Map).
- EMPTY = 0 -> Menandakan bahwa slot tersebut masih kosong dan belum pernah diisi data sama sekali.
- OCCUPIED = 1 -> Menandakan bahwa slot sedang aktif terisi oleh data (key dan value).
- DELETED = 2 -> Menandakan bahwa slot pernah terisi namun datanya sudah dihapus (berfungsi sebagai tombstone agar proses pencarian selanjutnya tidak terhenti secara prematur).

2. Class Entry (Digunakan untuk merepresentasikan satu entri data (pasangan kunci-nilai) di dalam Hash Map).
- def __init__(self): -> Merupakan konstruktor untuk menginisialisasi atribut objek Entry secara default.
- self.key = None -> Menginisialisasi kunci (dalam hal ini nama siswa) dengan nilai kosong/None.
- self.value = None -> Menginisialisasi nilai (dalam hal ini total nilai raport) dengan nilai kosong/None.
- self.state = SlotState.EMPTY -> Mengatur status awal entri menjadi kosong (EMPTY).
  
3.Class HashMapOpenAddressing (Berfungsi mengelola operasi struktur data Hash Map secara keseluruhan menggunakan teknik Open Addressing dan metode Linear Probing).
- def __init__(self, size=10): -> Konstruktor inisialisasi awal Hash Map dengan kapasitas default 10 (bisa diubah saat objek dibuat).
- self.SIZE = size -> Menyimpan ukuran kapasitas maksimal tabel.
- self.table = [Entry() for _ in range(self.SIZE)] -> Membuat array (list) berisi objek Entry baru sebanyak ukuran self.SIZE.
- def hash_function(self, key): -> Metode untuk menghasilkan indeks awal dari sebuah kunci menggunakan fungsi hash() bawaan Python.
- return (hash(key) % self.SIZE + self.SIZE) % self.SIZE -> Rumus untuk memastikan nilai indeks/hash selalu bernilai positif dan berada tepat di dalam rentang indeks tabel (0 sampai SIZE-1).
- def insert(self, key, value): -> Metode untuk menyisipkan data baru atau memperbarui data yang sudah ada di dalam tabel.
- idx = self.hash_function(key) -> Menentukan indeks awal berdasarkan key.
- first_deleted = -1 -> Variabel penanda untuk menyimpan indeks slot pertama yang berstatus DELETED yang ditemukan selama proses penelusuran (probing).
- for step in range(self.SIZE): -> Melakukan perulangan penelusuran maksimal sebanyak kapasitas tabel untuk mencari slot yang tepat.
- i = (idx + step) % self.SIZE -> Menghitung indeks pergeseran secara melingkar (linear probing).
- if self.table[i].state == SlotState.OCCUPIED: -> Jika slot terisi, program mengecek apakah kuncinya sama. Jika sama, nilainya langsung diperbarui (self.table[i].value = value).
- elif self.table[i].state == SlotState.DELETED: -> Jika menemui slot berstatus terhapus, indeksnya disimpan ke first_deleted agar bisa didaur ulang untuk memasukkan data baru jika ternyata kunci tersebut belum ada di tabel.
- else: -> Jika menemukan slot kosong (EMPTY), data dimasukkan ke slot tersebut (atau menggunakan slot first_deleted jika sebelumnya sudah ditemukan) dan statusnya diubah menjadi OCCUPIED.
- def search(self, key): -> Metode untuk mencari data berdasarkan kunci (nama). Melakukan probing sampai menemukan kunci yang cocok atau berhenti saat bertemu slot EMPTY. Mengembalikan objek Entry jika ketemu, atau None jika tidak.
- def remove_key(self, key): -> Metode untuk menghapus data berdasarkan kunci. Melakukan pencarian seperti metode search, jika ketemu, atribut key dan value diubah menjadi None, dan status diubah menjadi DELETED.
- def display(self): -> Metode untuk mencetak seluruh isi struktur tabel Hash Map ke layar beserta status tiap slotnya (EMPTY, DELETED, atau menampilkan isi datanya).

4. Fungsi main() (Digunakan sebagai program utama untuk menjalankan interaksi antarmuka CLI (Command Line Interface) dengan pengguna).
- report_hashmap = HashMapOpenAddressing(size=15) -> Membuat objek/ instance struktur Hash Map dengan kapasitas 15 elemen.
- while True: -> Memulai perulangan tanpa batas agar menu terus ditampilkan sampai pengguna memilih opsi keluar.
- choice = input(...) -> Menerima masukan dari pengguna untuk memilih operasi menu yang tersedia (angka 1 sampai 5).
- if choice == '1': -> Blok navigasi untuk fitur tambah/perbarui nilai.
- try ... except ValueError: -> Mekanisme Exception Handling untuk mencegah program crash (berhenti paksa) jika pengguna tidak sengaja memasukkan karakter non-angka saat diminta mengisi total nilai raport.
- elif choice == '2': -> Blok navigasi untuk mengeksekusi fitur pencarian nilai (search).
- elif choice == '3': -> Blok navigasi untuk mengeksekusi fitur penghapusan data (remove_key).
- elif choice == '4': -> Blok navigasi untuk memanggil metode display().
- elif choice == '5': -> Blok untuk menghentikan program menggunakan perintah break.
  
## d. Output Program

<img width="1294" height="735" alt="image" src="https://github.com/user-attachments/assets/ff22076d-9a68-40fd-a2ca-a621c8b5043c" />
<img width="543" height="698" alt="image" src="https://github.com/user-attachments/assets/01a79d59-172b-40b1-8abf-9ca0e91a3ce6" />
<img width="477" height="706" alt="image" src="https://github.com/user-attachments/assets/98f45aec-4580-49a1-8a2e-11f480bcab79" />
<img width="506" height="731" alt="image" src="https://github.com/user-attachments/assets/ef03496e-d393-4a31-8539-e91ff60cdc1f" />
<img width="511" height="873" alt="image" src="https://github.com/user-attachments/assets/852d0ed3-6ee4-4f06-ba45-0603ac679b0e" />
<img width="1116" height="569" alt="image" src="https://github.com/user-attachments/assets/02e07587-4569-41b1-bdd6-7122883c3c8c" />


1. Tampilan Menu Utama

Saat program pertama kali dijalankan, layar akan langsung menampilkan teks awalan berupa --- Menu Nilai Raport ---.

Program kemudian menampilkan 5 opsi tindakan (berbentuk teks CLI) yang bisa dipilih oleh pengguna, yaitu: Tambah Nilai Raport (Nama, Total Nilai), Cari Nilai Raport (Nama), Hapus Nilai Raport (Nama), Tampilkan Semua Nilai Raport, dan Keluar.

Input Pilihan Menu & Penanganan Error Pilihan

Setelah menu ditampilkan, program akan memunculkan prompt Pilih opsi (1-5):  dan menunggu pengguna mengetikkan angka pilihannya.

Jika pengguna memasukkan angka selain 1 hingga 5, atau memasukkan karakter acak pada prompt ini, program akan masuk ke kondisi else dan mencetak pesan peringatan "Opsi tidak valid. Silakan pilih antara 1 dan 5.", lalu memunculkan kembali menu utama secara berulang.

Tampilan Hasil Penambahan Nilai (Menu 1)

Jika pengguna mengetik angka 1, program akan meminta dua input secara berurutan: "Masukkan nama siswa: " dan "Masukkan total nilai raport: ".

Program sudah dibekali dengan penanganan error (try-except ValueError) khusus pada saat pengisian total nilai. Apabila pengguna mengetikkan huruf atau simbol (bukan angka), program tidak akan crash, melainkan mencetak pesan "Total nilai harus berupa angka." lalu kembali ke menu utama.

Jika eksekusi berhasil, program menampilkan pesan sukses: "Nilai raport [Nama] berhasil ditambahkan/diperbarui.". Namun, jika gagal karena array sudah terisi penuh (15 elemen terisi), akan muncul pesan "Gagal menambahkan nilai raport [Nama]. Mungkin tabel penuh.".

Tampilan Hasil Pencarian Nilai (Menu 2)

Jika pengguna mengetik angka 2, program memunculkan prompt "Masukkan nama siswa yang dicari: ".

Jika nama yang dicari ada di dalam tabel Hash Map, program akan mencetak output berupa: "Nilai raport [Nama]: [Total Nilai]".

Sebaliknya, jika pencarian menemui status EMPTY sebelum menemukan kunci yang pas, program akan mencetak pesan: "Nilai raport [Nama] tidak ditemukan.".

Tampilan Hasil Penghapusan Nilai (Menu 3)

Jika memilih menu 3, program memunculkan prompt "Masukkan nama siswa yang akan dihapus: ".

Apabila nama ditemukan dan statusnya berhasil diubah menjadi DELETED, akan tercetak pesan "Nilai raport [Nama] berhasil dihapus.".

Jika nama tersebut tidak ada di dalam sistem, program akan menampilkan "Nilai raport [Nama] tidak ditemukan atau gagal dihapus.".

Tampilan Isi Keseluruhan Tabel (Menu 4)

Saat memilih angka 4, layar akan mencetak judul Isi Hash Table (Open Addressing, Linear Probing): diikuti dengan daftar array dari indeks 0: hingga 14: (total 15 baris).

Status indeks yang belum pernah diisi akan tercetak sebagai EMPTY.

Status indeks yang datanya sudah dihapus via Menu 3 akan tercetak sebagai DELETED.

Status indeks yang memiliki data aktif akan menampilkan isi datanya dalam bentuk kordinat nilai, contoh: (Budi, 85).

Tampilan Keluar (Menu 5)

Jika pengguna memilih opsi 5, program mencetak baris perpisahan "Keluar dari menu Nilai Raport." lalu memanggil instruksi break yang akan mengakhiri perulangan (looping) dan menghentikan jalannya program secara otomatis.
## e. Link Youtube
https://youtu.be/u5HbIy0caXo
