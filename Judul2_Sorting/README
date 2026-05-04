#  Sistem Pemesanan Tiket Kapal (Linked List)

## a. Judul Program
Sistem Pemesanan Tiket Kapal Menggunakan Linked List

## b. Deskripsi Singkat
Program ini dirancang untuk mengelola antrean pemesanan tiket kapal dengan memanfaatkan struktur data Single Linked List. Melalui antarmuka menu, pengguna dapat menambahkan detail tiket baru, menampilkan seluruh daftar tiket yang sedang antre, dan memproses tiket yang berada pada urutan pertama. Sistem ini beroperasi berdasarkan prinsip First In First Out (FIFO), sehingga tiket yang pertama kali masuk ke dalam daftar akan diproses dan dikeluarkan lebih awal. Selain itu, program ini juga mengimplementasikan exception handling menggunakan blok try-except untuk menangani error dan memberikan peringatan apabila pengguna memasukkan format input menu yang tidak valid (bukan angka).

## c. Source Code
berikut adalah kode dari program pemesanan tiket kapal yang saya buat menggunakan linkedlist
<img width="544" height="840" alt="image" src="https://github.com/user-attachments/assets/711a68ce-d6bd-4f6e-b23a-31f673bf999a" />
<img width="781" height="722" alt="image" src="https://github.com/user-attachments/assets/38f32c0a-63f9-41e3-87c1-46903b6b73ac" />
<img width="489" height="421" alt="image" src="https://github.com/user-attachments/assets/927a5326-6ffd-4f7a-8f3e-79fb2caa6fd3" />

###  Penjelasan Kode
1. *Class Node*
   - Digunakan untuk merepresentasikan satu buah elemen (simpul) data tunggal di dalam memori.
   - Memiliki fungsi _init_ (konstruktor) untuk membuat node baru.
   - Memiliki atribut:
     - tiket → menyimpan data detail tiket kapal (seperti tujuan dan tanggal). 
     - next → pointer yang menunjuk ke node (tiket) berikutnya di dalam antrean bernilai awal None karena saat baru dibuat belum ada node lanjutan.

2. *Class LinkedList*
   - Digunakan untuk mengelola node-node tersebut agar saling menyambung dan membentuk struktur antrean tiket.
     Atribut:
     head menunjuk ke node pertama di dalam antrean. Saat objek LinkedList pertama kali dibuat, head bernilai None yang menandakan daftar masih kosong.
     
     Method tambah_tiket(self, tiket) :
- Bertugas menambahkan tiket baru ke urutan paling belakang (konsep Append).  
- Membungkus data input menjadi objek node baru (new_node = Node(tiket)).  
- Jika daftar masih kosong (self.head is None), maka head akan langsung menunjuk ke new_node.

    Method tampilkan_tiket(self) :
- Bertugas membaca dan menampilkan seluruh isi daftar tiket dari awal sampai akhir.  
- Mengecek apakah head adalah None; jika iya, program mencetak "Belum ada tiket.".  
- Jika tidak, program melakukan perulangan (while temp:) menelusuri dari head hingga akhir antrean, sekaligus mencetak nomor urut dan isi temp.tiket secara berurutan.

  Method proses_tiket(self) :
- Bertugas mengeksekusi dan menghapus tiket yang berada di paling depan antrean (konsep FIFO / First In First Out).  
- Jika daftar kosong, maka dicetak peringatan.  
- Jika ada isinya, program mencetak detail tiket yang diproses (self.head.tiket), kemudian memutus tiket tersebut dari antrean dengan cara menggeser pointer head ke node berikutnya (self.head = self.head.next).

3. *Fungsi menu()*
   Hanya sekadar menampilkan daftar pilihan menu (1 sampai 4) berbentuk teks di terminal untuk memudahkan pengguna.

4. *Fungsi main()*
- Menginisiasi antrean tiket dengan membuat objek daftar = LinkedList().
- Menggunakan perulangan tak terbatas (while True:) agar program terus berjalan dan selalu kembali ke menu utama setelah suatu perintah selesai dieksekusi.
- Menerapkan blok Exception Handling (try ... except ValueError:) saat meminta input pilihan menu.
- Jika pengguna menginput selain angka, program tidak akan mengalami error/crash, melainkan mencetak pesan peringatan dan mengulang perulangan (continue).  Percabangan if-elif-else untuk mengeksekusi pilihan pengguna:
Pilihan 1: Meminta input string dari pengguna mengenai detail tiket, lalu menyimpannya dengan memanggil fungsi daftar.tambah_tiket(tiket).  
Pilihan 2: Memanggil daftar.tampilkan_tiket().  
Pilihan 3: Memanggil daftar.proses_tiket() untuk memproses tiket terdepan.  
Pilihan 4: Mencetak "Program selesai." dan menggunakan perintah break untuk keluar dari perulangan while, yang otomatis mengakhiri jalannya program.  
else: Menangani jika pengguna memasukkan angka selain 1, 2, 3, atau 4.

5. *Blok if __name__ == "__main__":*
Digunakan sebagai pengecekan standar di Python. Ini memastikan bahwa fungsi main() hanya akan dieksekusi jika file Python dijalankan secara langsung (bukan diimpor sebagai modul ke dalam file proyek lain).

## d. Output Program

<img width="697" height="819" alt="image" src="https://github.com/user-attachments/assets/2dfefaba-0ee8-444e-8f1f-03d38b702927" />
<img width="454" height="788" alt="image" src="https://github.com/user-attachments/assets/f309a170-1ccd-4732-be5f-a29460d710a0" />

1. Penanganan Input Menu Utama
  - Saat user memasukkan huruf atau simbol (bukan angka) muncul pesan "Input harus angka!" dan program akan mengulang tampilan menu dari awal.
  - Saat user memasukkan angka selain 1, 2, 3, atau 4 muncul pesan "Pilihan tidak valid!".
2. Menu 1: Tambah Tiket
  - Saat user memilih menu 1 dan memasukkan detail tiket muncul pesan konfirmasi bahwa tiket telah masuk ke dalam memori.
3. Menu 2: Tampilkan Tiket
  - Saat user memilih menu 2, tetapi daftar antrean masih kosong muncul pesan "Belum ada tiket.".
  - Saat user memilih menu 2, dan sudah ada tiket di dalam antrean muncul judul "\nDaftar Tiket:" diikuti dengan daftar seluruh tiket secara berurutan beserta nomor urutnya.
4. Menu 3: Proses Tiket Pertama
  - Saat user memilih menu 3, tetapi daftar antrean masih kosong muncul pesan "Tidak ada tiket.".
  - Saat user memilih menu 3, dan terdapat tiket di dalam antrean tiket yang berada di urutan paling atas (nomor 1) akan dihapus dari antrean dan muncul pesan konfirmasi.
5. Menu 4: Keluar
  - Saat user memilih menu 4 muncul pesan "Program selesai." dan eksekusi program akan langsung dihentikan.

## e. Link Youtube

https://youtu.be/IEe3KP_S1-k?si=ieiIPAprOH3K7VUB
