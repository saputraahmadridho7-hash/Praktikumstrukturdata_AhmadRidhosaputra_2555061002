#  Manajemen Buku Perpustakaan (Binary Search Tree)

## a. Judul Program
Membuat Manajemen Buku Perpustakaan Menggunakan Binary Search Tree

## b. Deskripsi Singkat
Program ini dirancang untuk menyimulasikan sistem manajemen perpustakaan secara dinamis dengan memanfaatkan struktur data Binary Search Tree (BST). Sistem ini beroperasi secara terstruktur menggunakan nomor ISBN (International Standard Book Number) sebagai penentu arah (key) untuk menyisipkan setiap data buku ke posisi kiri (jika ISBN lebih kecil) atau kanan (jika ISBN lebih besar) dari titik acuan atau node induknya. Penggunaan hierarki pohon biner ini membuat manajemen data menjadi sangat efisien karena elemen-elemen tersusun secara berurutan, sehingga mempercepat proses pencarian, penyisipan, maupun penghapusan data buku. Program ini dilengkapi dengan fitur tingkat lanjut untuk menelusuri seluruh buku secara terstruktur dari atas ke bawah (level-order traversal) menggunakan bantuan struktur data antrean (queue), mengkalkulasi tinggi pohon (kedalaman data), serta melacak buku dengan nomor ISBN tepat sebelum (predecessor) atau sesudah (successor) buku tertentu. Di samping itu, program ini juga mengimplementasikan mekanisme exception handling menggunakan blok try-except pada saat menerima masukan navigasi menu dan atribut buku dari pengguna untuk menangani potensi error (seperti ValueError), sehingga program tetap berjalan stabil dan mencegah crash saat pengguna memasukkan tipe data yang tidak valid.

## c. Source Code
berikut adalah kode dari program MMembuat Manajemen Buku Perpustakaan Menggunakan Binary Search Tree
<img width="1127" height="882" alt="image" src="https://github.com/user-attachments/assets/12124592-e59c-403b-888b-0284b9a3983c" />
<img width="1012" height="836" alt="image" src="https://github.com/user-attachments/assets/dda53a87-1d7c-4716-840f-9e307a12a82e" />
<img width="618" height="815" alt="image" src="https://github.com/user-attachments/assets/40896556-1d7b-4dcb-b7a4-0bd449f0eb66" />
<img width="711" height="816" alt="image" src="https://github.com/user-attachments/assets/6570d88e-cd8d-4c2f-9749-9420dec69745" />
<img width="850" height="837" alt="image" src="https://github.com/user-attachments/assets/f47a33d2-3485-4899-a1e4-220a03c0495c" />
<img width="996" height="812" alt="image" src="https://github.com/user-attachments/assets/f90025da-ee64-415a-a29d-0fb607cddc66" />
<img width="1276" height="805" alt="image" src="https://github.com/user-attachments/assets/d701524a-d731-408a-95fa-7c92ec2590cb" />
<img width="457" height="113" alt="image" src="https://github.com/user-attachments/assets/160a149e-431a-474b-8e57-f9e8cf654f13" />


###  Penjelasan Kode
1. Class Book (Digunakan sebagai struktur dasar untuk merepresentasikan objek data buku).
- def __init__(self, isbn, title, author, book_type): -> Merupakan konstruktor untuk menginisialisasi atribut objek Book setiap kali buku baru dibuat.
- self.isbn = isbn -> Mengisi atribut isbn pada objek dengan nilai dari parameter isbn.
- self.title = title -> Mengisi atribut title dengan nilai parameter title.
- self.author = author -> Mengisi atribut author dengan nilai parameter author.
- self.book_type = book_type -> Mengisi atribut book_type untuk menyimpan jenis buku (Fisik/Digital).
- def __str__(self): -> Metode bawaan untuk mengatur format saat objek buku dicetak (di-print).
- return f"ISBN: {self.isbn}, Judul: ..." -> Mengembalikan representasi string dari informasi buku agar mudah dibaca oleh pengguna.

2. Class Node (Digunakan untuk merepresentasikan satu simpul elemen di dalam Binary Search Tree (BST)).
- def __init__(self, book): -> Konstruktor inisialisasi simpul (node).
- self.book = book -> Menyimpan objek Book (yang berisi ISBN, dll) ke dalam bagian data node ini.
- self.left = None -> Pointer ke node anak cabang kiri, diinisialisasi None karena belum terhubung.
- self.right = None -> Pointer ke node anak cabang kanan, diinisialisasi None.

3. Class LibraryBST (Berfungsi mengelola operasi struktur data Binary Search Tree secara keseluruhan.)
- def __init__(self): -> Konstruktor inisialisasi awal pohon.
- self.root = None -> Menetapkan root (akar) pohon bernilai None, menandakan perpustakaan masih kosong.
- def _insert_book_node(self, root, book): -> Fungsi rekursif (memanggil dirinya sendiri) untuk mencari posisi penempatan buku baru.
- if root is None: return Node(book) -> Basis Rekursi: Jika posisi node saat ini kosong, buat dan letakkan Node baru di situ.
- if book.isbn < root.book.isbn: -> Jika ISBN buku baru lebih kecil dari ISBN node saat ini.
- root.left = self._insert_book_node(root.left, book) -> Arahkan proses penyisipan ke cabang kiri (root.left).
- elif book.isbn > root.book.isbn: -> Jika ISBN buku baru lebih besar.
- root.right = self._insert_book_node(root.right, book) -> Arahkan proses penyisipan ke cabang kanan (root.right).
- return root -> Mengembalikan node ke tingkat sebelumnya agar pohon tersambung utuh.

- def add_book(self, book): -> Fungsi pemanggil untuk menambah buku.
- self.root = self._insert_book_node(self.root, book) -> Memulai proses penyisipan dari self.root (paling atas).
- def _find_min_node(self, node): -> Fungsi mencari node dengan ISBN terkecil di sebuah cabang.
- current = node -> Set titik awal pencarian.
- while current is not None and current.left is not None: current = current.left -> Selama cabang kiri masih ada, terus geser ke kiri sampai mentok (karena nilai terkecil di BST selalu paling kiri).
- return current -> Kembalikan node paling ujung kiri.
- def _delete_book_node(self, root, isbn): -> Fungsi rekursif untuk menghapus node buku.
- if root is None: return None -> Jika pohon kosong atau buku tak ditemukan, hentikan proses.
- if isbn < root.book.isbn: root.left = self._delete_book_node(root.left, isbn) -> Jika ISBN yang mau dihapus lebih kecil, cari di cabang kiri.
- elif isbn > root.book.isbn: root.right = self._delete_book_node(root.right, isbn) -> Jika lebih besar, cari di cabang kanan.
- else: -> Kondisi ketika node dengan ISBN yang tepat telah ditemukan. Terdapat 3 kondisi penanganan:
- if root.left is None and root.right is None: return None -> Kondisi 1: Node tidak punya anak (daun). Langsung dihapus dengan cara mengembalikan None.
- elif root.left is None: return root.right -> Kondisi 2: Node hanya punya anak kanan. Hubungkan langsung dengan anak kanannya.
- elif root.right is None: return root.left -> Kondisi 2: Node hanya punya anak kiri. Hubungkan langsung dengan anak kirinya.
- else: -> Kondisi 3: Node punya dua anak cabang.
- successor = self._find_min_node(root.right) -> Cari nilai pengganti terkecil (successor) dari cabang kanannya.
- root.book = successor.book -> Gantikan isi data buku yang dihapus dengan data buku successor.
- root.right = self._delete_book_node(root.right, successor.book.isbn) -> Hapus node successor di bawahnya (karena datanya sudah dipindah ke atas).
- def remove_book(self, isbn): -> Fungsi pemanggil penghapusan buku.
- self.root = self._delete_book_node(self.root, isbn) -> Mulai proses penghapusan dari akar pohon.
- def search_book(self, isbn): -> Fungsi mencari buku secara berulang (iteratif).
- current = self.root -> Titik awal dari puncak.
- while current is not None: -> Terus lakukan pencarian selama belum menemui jalan buntu (None).
- if isbn == current.book.isbn: return current.book -> Jika ISBN persis sama, kembalikan objek bukunya.
- elif isbn < current.book.isbn: current = current.left -> Jika ISBN lebih kecil, geser pencarian ke anak kiri.
- else: current = current.right -> Jika ISBN lebih besar, geser pencarian ke anak kanan.
- return None -> Kembalikan kosong jika ISBN sama sekali tidak ada di pohon.
- def get_height(self, root): -> Fungsi mencari kedalaman/tinggi maksimal pohon.
- if root is None: return -1 -> Basis rekursi, menyeimbangkan nilai root agar dihitung sebagai 0 jika hanya punya 1 simpul.
- height_left = self.get_height(root.left) -> Cari tinggi maksimal cabang kiri.
- height_right = self.get_height(root.right) -> Cari tinggi maksimal cabang kanan.
- return 1 + max(height_left, height_right) -> Ambil nilai terbesar antara kiri dan kanan, lalu tambahkan 1 (untuk tinggi node itu sendiri).
- def list_all_books_level_order(self): -> Fungsi menelusuri secara mendatar tingkat demi tingkat.
- queue = [] -> Membuat struktur antrean menggunakan list kosong.
- queue.append(self.root) -> Memasukkan node pertama (root) ke dalam antrean.
- while len(queue) > 0: -> Lakukan perulangan selama antrean belum kosong.
- current = queue.pop(0) -> Mengeluarkan (pop) elemen paling depan (indeks 0) dari antrean untuk diproses.
- print(current.book) -> Cetak elemen yang baru saja dikeluarkan.
- if current.left is not None: queue.append(current.left) -> Jika punya anak kiri, masukkan anak kiri ke belakang antrean.
- if current.right is not None: queue.append(current.right) -> Jika punya anak kanan, masukkan ke belakang antrean.
- def find_successor_book(self, target_isbn): -> Fungsi lengkap mencari buku penerus (nilai tepat lebih besar).
- book_found = self.search_book(target_isbn) -> Cek dulu keberadaan buku yang dicari.
- if book_found is None: return self._find_successor_isbn(self.root, target_isbn) -> Jika buku target tidak ada, cari secara manual dari root memakai fungsi _find_successor_isbn.
- while current is not None: -> Loop mencari posisi node dari target.
- if target_isbn < current.book.isbn: successor_node = current; current = current.left -> Node yang lebih besar dari target disimpan sementara - di variabel successor_node, lalu teruskan pencarian ke kiri.
- elif target_isbn > current.book.isbn: current = current.right -> Terus ke kanan.
- else: -> Jika posisi persis node target ketemu:
- if current.right is not None: return self._find_min_node(current.right).book -> Kunci: Successor dari node yang punya cabang kanan, adalah anak paling kiri (nilai terkecil) dari cabang kanannya itu.
- def find_predecessor_book(self, target_isbn): -> Sama seperti successor, namun mencari nilai pendahulu (tepat lebih kecil).
- if current.left is not None: temp = current.left; while temp.right is not None: temp = temp.right; return temp.book -> Kunci: Predecessor dari node yang punya cabang kiri, adalah anak paling kanan (nilai terbesar) dari cabang kirinya.

4. def main() Fungsi pelaksana interaksi dengan pengguna (User Interface berbasis teks).
- library = LibraryBST() -> Membuat instansi perpustakaan baru.
- while pilih != 8: -> Memulai perulangan menu tanpa akhir hingga dipilih opsi 8.
- try... except ValueError: -> Blok perlindungan program dari potensi kerusakan. Jika di dalam bagian try (yakni saat minta int(input())) pengguna memasukkan huruf, maka program melompat ke except dan mencetak "Input tidak valid" tanpa menjadi error.
- if pilih == 1: -> Proses input buku baru.
- if book_type not in ['Fisik', 'Digital']: continue -> Pengecekan ketat (validasi), jika teks bukan salah satu dari keduanya, maka pendaftaran dibatalkan dan mengulang dari atas (continue).
- elif pilih == 2: -> Fitur Hapus. Dicek dulu lewat library.search_book(isbn_to_delete). Jika found_book mengembalikan objek (ada isinya), eksekusi library.remove_book, jika tidak, cetak pesan gagal.
- elif pilih == 3: -> Kondisi ketika pengguna memilih opsi 3 (Mencari Buku).
- isbn_to_search = input("Masukkan ISBN buku yang dicari: ") -> Program meminta pengguna memasukkan ISBN buku yang ingin dicari, lalu menyimpannya dalam variabel isbn_to_search.
- found_book = library.search_book(isbn_to_search) -> Program memanggil fungsi search_book pada objek library dan menyimpan hasilnya (objek buku atau None) di variabel found_book.
- if found_book: -> Memeriksa apakah found_book berisi data (buku berhasil ditemukan).
- print("Buku ditemukan:") dan print(f"  {found_book}") -> Jika ada, program mencetak teks penanda dan mencetak detail informasi buku tersebut (otomatis memanggil fungsi __str__ pada Class Book).
- else: -> Jika found_book bernilai None (buku tidak ada di dalam pohon).
- print(f"Buku dengan ISBN '{isbn_to_search}' tidak ditemukan.") -> Mencetak pesan bahwa buku yang dicari tidak tersedia.
- elif pilih == 4: -> Kondisi ketika pengguna memilih opsi 4 (Daftar Semua Buku).
- print("\nDaftar semua buku (Level-order):") -> Mencetak judul atau tajuk daftar buku.
- library.list_all_books_level_order() -> Memanggil fungsi untuk menelusuri dan mencetak seluruh isi pohon secara horizontal (level demi level).
- elif pilih == 5: -> Kondisi ketika pengguna memilih opsi 5 (Tinggi Pohon).
- print(f"Tinggi pohon BST: {library.get_height(library.root)}") -> Program langsung mencetak string berformat yang memanggil fungsi get_height dengan memasukkan library.root (akar pohon) sebagai titik awal perhitungan kedalaman struktur pohon.
- elif pilih == 6: -> Kondisi ketika pengguna memilih opsi 6 (Cari Successor).
- isbn_target = input("Cari successor dari ISBN: ") -> Meminta pengguna memasukkan ISBN yang akan dijadikan patokan.
- successor = library.find_successor_book(isbn_target) -> Memanggil fungsi untuk mencari buku dengan ISBN yang nilainya tepat lebih besar satu tingkat dari isbn_target.
- if successor: -> Jika buku penerusnya ditemukan.
- print(f"Successor dari ISBN {isbn_target}:\n  {successor}") -> Menampilkan detail informasi buku penerus tersebut.
- else: -> Jika nilai balikan fungsi adalah None.
- print(f"Tidak ada successor untuk ISBN {isbn_target} (mungkin ISBN tidak ada atau yang terbesar).") -> Mencetak pesan bahwa successor tidak ada (bisa jadi karena ISBN patokan tidak terdaftar, atau patokan itu sendiri adalah buku dengan ISBN paling besar di sistem).
- elif pilih == 7: -> Kondisi ketika pengguna memilih opsi 7 (Cari Predecessor).
- isbn_target = input("Cari predecessor dari ISBN: ") -> Meminta pengguna memasukkan ISBN patokan.
- predecessor = library.find_predecessor_book(isbn_target) -> Memanggil fungsi untuk mencari buku dengan ISBN yang nilainya tepat lebih kecil dari isbn_target (pendahulu).
- if predecessor: -> Jika buku pendahulunya ada.
- print(f"Predecessor dari ISBN {isbn_target}:\n  {predecessor}") -> Menampilkan detail informasi buku pendahulu tersebut.
- else: -> Jika tidak ditemukan.
- print(f"Tidak ada predecessor untuk ISBN {isbn_target} (mungkin ISBN tidak ada atau yang terkecil).") -> Mencetak pesan bahwa predecessor tidak ada.
- elif pilih == 8: -> Kondisi ketika pengguna memilih opsi 8 (Keluar).
- print("Program Sistem Manajemen Perpustakaan selesai.") -> Mencetak pesan perpisahan. Setelah ini, program akan kembali ke atas perulangan while, namun karena pilih sekarang bernilai 8, maka syarat while pilih != 8: menjadi bernilai Salah (False), sehingga perulangan (dan program) otomatis berhenti.
- else: -> Kondisi "sapu jagat" jika pengguna secara tidak sengaja memasukkan angka selain 1 hingga 8 (misalnya memasukkan angka 9).
- print("Pilihan tidak valid!") -> Program memberi tahu bahwa menu tersebut tidak ada, dan perulangan while akan terus berlanjut untuk meminta input kembali.
- if __name__ == "__main__": -> Ini adalah standar baku (idiom) dalam penulisan program Python.
- main() -> Pemanggilan fungsi utama. Blok ini memastikan bahwa fungsi main() (yang berisi menu dan perulangan interaktif di atas) hanya akan dijalankan jika kamu menjalankan (run) file BSTLanjut.py ini secara langsung. Jika file kode ini suatu saat di-import sebagai modul/pustaka ke dalam file kode Python lainnya, program interaktifnya tidak akan tiba-tiba berjalan sendiri.
  
## d. Output Program

<img width="1294" height="735" alt="image" src="https://github.com/user-attachments/assets/ff22076d-9a68-40fd-a2ca-a621c8b5043c" />
<img width="543" height="698" alt="image" src="https://github.com/user-attachments/assets/01a79d59-172b-40b1-8abf-9ca0e91a3ce6" />
<img width="477" height="706" alt="image" src="https://github.com/user-attachments/assets/98f45aec-4580-49a1-8a2e-11f480bcab79" />
<img width="506" height="731" alt="image" src="https://github.com/user-attachments/assets/ef03496e-d393-4a31-8539-e91ff60cdc1f" />
<img width="511" height="873" alt="image" src="https://github.com/user-attachments/assets/852d0ed3-6ee4-4f06-ba45-0603ac679b0e" />
<img width="1116" height="569" alt="image" src="https://github.com/user-attachments/assets/02e07587-4569-41b1-bdd6-7122883c3c8c" />


1. Tampilan Menu Utama
- Saat program pertama kali dijalankan, layar akan langsung menampilkan daftar menu antarmuka teks (CLI) dengan judul === Sistem Manajemen Perpustakaan ===.
- Program menampilkan 8 opsi tindakan yang bisa dipilih oleh pengguna, yaitu: Tambah Buku, Hapus Buku, Cari Buku (berdasarkan ISBN), Daftar Semua Buku (Level-order), Tinggi Pohon, Cari Successor (berdasarkan ISBN), Cari Predecessor (berdasarkan ISBN), dan Keluar.

2. Input Pilihan Menu & Penanganan Error
- Setelah menu ditampilkan, program akan memunculkan prompt Pilih: dan menunggu pengguna untuk mengetikkan angka pilihan.
- Program sudah dibekali dengan penanganan error (try-except ValueError). Apabila pengguna memasukkan karakter selain angka (misalnya huruf atau simbol), program tidak akan crash, melainkan memunculkan pesan peringatan "Input tidak valid! Masukkan angka." lalu memunculkan kembali menu utama.
- Jika pengguna memasukkan angka selain 1 hingga 8, program akan mencetak peringatan "Pilihan tidak valid!".

3. Tampilan Hasil Penambahan Buku (Menu 1)
- Jika pengguna mengetik angka 1, program akan meminta empat baris input secara berurutan: "Masukkan ISBN buku:", "Masukkan Judul buku:", "Masukkan Penulis buku:", dan "Masukkan Tipe buku (Fisik/Digital):".
- Terdapat validasi ketat pada input tipe buku. Jika teks yang dimasukkan bukan 'Fisik' atau 'Digital', program mencetak peringatan: "Tipe buku tidak valid! Harus 'Fisik' atau 'Digital'." lalu pendaftaran dibatalkan.
- Setelah data yang valid dimasukkan, program akan mencetak pesan keberhasilan: "Buku '[judul]' (ISBN: [isbn]) berhasil ditambahkan."

4. Tampilan Hasil Penghapusan & Pencarian (Menu 2 & 3)
- Hapus Buku (Menu 2): Program akan meminta input ISBN yang ingin dihapus. Jika ISBN tersebut ada di dalam sistem, program menghapusnya dan mencetak "Buku dengan ISBN '[isbn]' berhasil dihapus.". Jika tidak ada, program mencetak "Buku dengan ISBN '[isbn]' tidak ditemukan."
- Cari Buku (Menu 3): Program meminta input ISBN. Jika buku ditemukan, mencetak "Buku ditemukan:" dilanjutkan dengan detail format bukunya (ISBN, Judul, Penulis, Tipe). Jika gagal, memunculkan notifikasi bahwa buku tidak ditemukan.

5. Tampilan Daftar Buku & Tinggi Pohon (Menu 4 & 5)
- Daftar Semua Buku (Menu 4): Program akan mencetak judul "\nDaftar semua buku (Level-order):". Selanjutnya program akan menampilkan seluruh data buku secara terstruktur berurutan dari akar hingga ke daun. Jika belum ada buku sama sekali, program menampilkan "(Perpustakaan kosong)".
- Tinggi Pohon (Menu 5): Program akan mengkalkulasi lalu langsung mencetak informasi kedalaman pohon dengan format "Tinggi pohon BST: [angka]".

6. Tampilan Hasil Pencarian Lanjutan (Menu 6 & 7)
- Successor (Menu 6): Program meminta ISBN target. Jika buku penerusnya (successor) ditemukan, akan dicetak "Successor dari ISBN [isbn]:" disusul detail bukunya. Jika tidak (misal buku itu adalah yang paling besar nilainya), akan muncul: "Tidak ada successor untuk ISBN [isbn] (mungkin ISBN tidak ada atau yang terbesar)."
- Predecessor (Menu 7): Sama halnya dengan successor, program akan mencari buku pendahulunya. Jika tidak ditemukan, akan memberikan peringatan: "Tidak ada predecessor untuk ISBN [isbn] (mungkin ISBN tidak ada atau yang terkecil)."
  
## e. Link Youtube
https://youtu.be/WzZOGZcMkFo
