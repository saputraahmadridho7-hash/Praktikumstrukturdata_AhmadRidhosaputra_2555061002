#  Membuat Antrian Tiket Kereta Api (Queue Linkedlist)

## a. Judul Program
Membuat Antrian Tiket Kereta Api Menggunakan Queue Linkedlist

## b. Deskripsi Singkat
Program ini dirancang untuk menyimulasikan sistem antrean pemesanan tiket kereta api secara dinamis dengan memanfaatkan struktur data Queue (Antrean) yang diimplementasikan berbasis Single Linked List. Sistem ini beroperasi secara terstruktur menggunakan dua titik acuan utama, yaitu front pointer untuk melacak dan memproses tiket penumpang terdepan (dequeue) serta rear pointer untuk menyisipkan data penumpang baru beserta tujuannya ke posisi paling belakang (enqueue). Penggunaan linked list ini membuat manajemen data menjadi sangat fleksibel karena elemen-elemen dihubungkan melalui node sehingga ukuran antrean dapat bertambah atau berkurang. program ini dilengkapi dengan fitur untuk menghitung estimasi waktu tunggu penumpang secara otomatis dan memantau status antrean untuk memberikan peringatan dini jika antrean terdeteksi padat. Di samping itu, program ini juga mengimplementasikan mekanisme exception handling menggunakan blok try-except pada saat menerima masukan navigasi menu dari pengguna untuk menangani potensi error (seperti ValueError), sehingga program tetap berjalan stabil dan menginstruksikan pengguna untuk mengulang kembali jika masukan yang diberikan tidak valid.

## c. Source Code
berikut adalah kode dari program Mencari Nama Mahasiswa Menggunakan sequential search sentinel
<img width="1220" height="889" alt="image" src="https://github.com/user-attachments/assets/3da3161c-ab24-4d64-b484-0efac8f805a7" />
<img width="1078" height="808" alt="image" src="https://github.com/user-attachments/assets/5f25db67-4da3-4844-bd60-0bcaeff11246" />
<img width="1174" height="827" alt="image" src="https://github.com/user-attachments/assets/0a0c126e-eeb8-410f-8b59-b7688147a72b" />
<img width="883" height="370" alt="image" src="https://github.com/user-attachments/assets/8391de37-24f7-4105-8fa0-516988929db7" />


###  Penjelasan Kode
1. Class Node

- Digunakan sebagai struktur dasar untuk merepresentasikan satu elemen (simpul) tunggal di dalam struktur data Linked List.
- def __init__(self, data): -> Merupakan konstruktor untuk menginisialisasi objek Node baru setiap kali ada tiket yang ditambahkan.
- self.data = data -> Atribut untuk menyimpan nilai informasi penumpang (berupa dictionary yang berisi nama dan tujuan).
- self.next = None -> Atribut pointer (penunjuk) yang menunjuk ke node selanjutnya dalam antrean. Diinisialisasi dengan nilai None karena saat dibuat, node tersebut belum terhubung ke mana pun.

2. Class QueueLinkedList

- Berfungsi untuk mengelola struktur data antrean (Queue) secara keseluruhan yang diimplementasikan menggunakan konsep Single Linked List.
- def __init__(self): -> Konstruktor untuk menetapkan keadaan atau status awal dari antrean tiket.
- self.front_ptr = None dan self.rear_ptr = None -> Menginisialisasi pointer bagian depan (front) dan belakang (rear) dengan None, yang menandakan bahwa antrean masih dalam keadaan kosong.
- self.size = 0 -> Variabel counter untuk melacak jumlah total tiket/penumpang yang saat ini sedang mengantre.
- self.processing_time_per_ticket = 2 -> Menetapkan waktu estimasi (dalam menit) yang dibutuhkan untuk memproses satu tiket, digunakan nantinya untuk menghitung total waktu tunggu.
- Fungsi is_empty(self): -> Mengevaluasi dan mengembalikan nilai boolean (True/False) dengan mengecek apakah front_ptr bernilai None untuk mengetahui antrean kosong atau tidak.
- Fungsi enqueue(self, nama, tujuan): -> Berfungsi untuk menambahkan data penumpang baru ke urutan paling belakang dari antrean.
- ticket = {'nama': nama, 'tujuan': tujuan} -> Membungkus data inputan nama dan tujuan ke dalam struktur dictionary sebelum dimasukkan ke dalam node.
- self.rear_ptr.next = new_node -> Menghubungkan node yang sebelumnya berada di paling belakang dengan node yang baru saja dibuat, sehingga antrean tersambung.
- Fungsi dequeue(self): -> Digunakan untuk memproses dan mengeluarkan elemen yang berada di urutan paling depan dari antrean.
- self.front_ptr = self.front_ptr.next -> Inti dari proses dequeue; menggeser pointer depan ke node selanjutnya, yang secara logis akan membuang node pertama dari linked list.
- Fungsi peek(self): -> Mengambil dan menampilkan data tiket yang berada di urutan paling depan tanpa menghapus atau mengeluarkannya dari antrean.
- Fungsi display(self): -> Melakukan perulangan (iterasi) mulai dari front_ptr hingga node bernilai None (akhir antrean) untuk mencetak seluruh isi daftar antrean beserta status kelancarannya.
- Fungsi calculate_wait_time(self): -> Mengkalkulasi estimasi waktu tunggu dengan mengalikan jumlah elemen saat ini (self.size) dengan waktu proses per tiket.

3. Fungsi main()

- Bertugas sebagai program utama untuk mendeklarasikan objek antrean, mengelola interaksi antarmuka teks (menu input/output) dengan pengguna, dan memanggil fungsi-fungsi queue yang sesuai.
- queue = QueueLinkedList() -> Mendeklarasikan objek queue sebagai instansiasi baru dari class QueueLinkedList.
- while pilih != 6: -> Perulangan utama program yang akan terus menampilkan menu antrean kereta api selama pengguna tidak menginputkan angka 6 (Keluar).
- Blok try...except ValueError: -> Mengimplementasikan penanganan kesalahan (exception handling) untuk mencegah program error atau berhenti mendadak jika pengguna memasukkan karakter yang bukan angka (huruf/simbol) pada saat memilih menu.
- if pilih == 1: hingga elif pilih == 6: -> Merupakan struktur percabangan untuk mengeksekusi metode di dalam objek queue (seperti enqueue, dequeue, display, dll) sesuai dengan nomor menu yang diketikkan pengguna.

## d. Output Program

<img width="723" height="805" alt="image" src="https://github.com/user-attachments/assets/92474b74-736d-4acb-a3ee-32df9d0918c3" />
<img width="734" height="717" alt="image" src="https://github.com/user-attachments/assets/c4e8d069-cfcc-4ca9-9598-12d8991bc399" />
<img width="674" height="531" alt="image" src="https://github.com/user-attachments/assets/366169c2-a294-489e-adf7-28559f29e5c3" />


1. Tampilan Menu Utama
- Saat program pertama kali dijalankan, layar akan langsung menampilkan daftar menu antarmuka teks (CLI) dengan judul === ANTRIAN TIKET KERETA API (Linked List) ===.
- Program menampilkan 6 opsi tindakan yang bisa dipilih oleh pengguna, yaitu: Tambah Tiket (Enqueue), Keluarkan Tiket (Dequeue), Lihat Tiket Terdepan (Peek), Tampilkan Antrean, Hitung Estimasi Waktu Tunggu, dan Keluar.

2. Input Pilihan Menu & Penanganan Error
- Setelah menu ditampilkan, program akan memunculkan prompt Pilih:  dan menunggu pengguna untuk mengetikkan angka.
- Program sudah dibekali dengan penanganan error (try-except ValueError). Apabila pengguna memasukkan karakter selain angka (misalnya huruf atau simbol), program tidak akan crash, melainkan memunculkan pesan peringatan "Input tidak valid! Masukkan angka antara 1-6." lalu memunculkan kembali menu utama.

3. Tampilan Hasil Penambahan Tiket (Menu 1)
- Jika pengguna mengetik angka 1, program akan meminta dua input: "Masukkan nama penumpang:" dan "Masukkan tujuan kereta:". Terdapat validasi yang mencegah inputan kosong.
- Setelah data valid dimasukkan, program akan mencetak pesan keberhasilan: "Tiket untuk [nama] tujuan [tujuan] berhasil ditambahkan ke antrean."
- Jika ukuran antrean sudah mencapai 5 tiket atau lebih, program akan memunculkan teks tambahan: "PERINGATAN: Antrean tiket sangat padat, mohon percepat pelayanan!" sebagai pengingat visual.

4. Tampilan Hasil Pemrosesan Tiket (Menu 2 & 3)
- Keluarkan Tiket (Menu 2): Jika ada antrean, program akan mengeluarkan tiket urutan pertama dan mencetak "Tiket untuk [nama] tujuan [tujuan] berhasil dikeluarkan dari antrean.". Jika antrean kosong, program mencetak "Antrean tiket kosong".
- Lihat Tiket Terdepan (Menu 3): Program hanya menampilkan data penumpang urutan pertama tanpa menghapusnya dari memori, dengan format "Tiket terdepan: [nama] dengan tujuan [tujuan]".

5. Tampilan Status Keseluruhan & Estimasi Waktu (Menu 4 & 5)
- Tampilkan Antrean (Menu 4): Program mencetak daftar seluruh tiket yang sedang mengantre secara berurutan (dari indeks 1 dst.) dengan format "1. Nama: [nama], Tujuan: [tujuan]". Di bagian bawah daftar, program akan menampilkan indikator "Status antrean: Padat" (jika tiket $\ge$ 5) atau "Status antrean: Lancar"
- .Hitung Estimasi Waktu (Menu 5): Program akan mengkalkulasi waktu (jumlah tiket $\times$ 2 menit) dan mencetak hasilnya ke layar: "Estimasi waktu tunggu saat ini: [X] menit untuk [Y] tiket."

6. Tampilan Keluar Program (Menu 6)
- Saat pengguna memilih angka 6 untuk keluar, program akan melakukan pembersihan data (clearing) dengan mengeluarkan (mencetak proses dequeue) seluruh tiket yang masih tersisa di dalam antrean satu per satu.
- Setelah antrean benar-benar bersih, program akan mencetak kalimat penutup "Program antrean tiket selesai. Sampai jumpa!" dan eksekusi program pun resmi dihentikan.

  
## e. Link Youtube
https://youtu.be/kQpL-u26s7Y
