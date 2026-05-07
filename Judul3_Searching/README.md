#  Mencari Nama Mahasiswa (sequential search sentinel)

## a. Judul Program
Mencari Nama Mahasiswa Menggunakan sequential search sentinel

## b. Deskripsi Singkat
Program ini dirancang untuk melakukan pencarian data nama mahasiswa dari program studi PSTI D di dalam sebuah kumpulan data (array) yang telah ditentukan, dengan memanfaatkan algoritma Sequential Search berbasis Sentinel. Sistem ini beroperasi secara efisien dengan cara menambahkan elemen target yang ingin dicari ke posisi paling akhir dari array sebagai "sentinel" (penjaga). Penambahan sentinel ini memungkinkan proses perulangan berjalan lebih cepat karena mengeliminasi kebutuhan untuk terus-menerus memeriksa batas indeks array pada setiap langkah evaluasi. Setelah proses pencarian berhenti pada elemen yang cocok, program kemudian membuang sentinel tersebut dan mengevaluasi apakah indeks kecocokan berada di dalam rentang data asli untuk menyimpulkan apakah nama tersebut benar-benar ditemukan atau tidak. Selain itu, program ini juga mengimplementasikan mekanisme exception handling menggunakan blok try-except pada saat menerima masukan dari pengguna untuk menangani potensi error, sehingga program dapat memberikan peringatan untuk mengulang kembali jika masukan dianggap tidak valid.

## c. Source Code
berikut adalah kode dari program Mencari Nama Mahasiswa Menggunakan sequential search sentinel
<img width="1411" height="523" alt="image" src="https://github.com/user-attachments/assets/a7a83656-965d-4677-9865-4cddec58d771" />
<img width="1014" height="322" alt="image" src="https://github.com/user-attachments/assets/286380ed-63e5-408c-aea2-65d4e95bb49f" />


###  Penjelasan Kode
1. Fungsi sequential_search_sentinel(data, n, target)
- Digunakan untuk melakukan pencarian sebuah elemen (nama mahasiswa) di dalam list menggunakan algoritma Sequential Search dengan teknik Sentinel.
- data.append(target) -> Menambahkan elemen yang dicari (target) ke bagian paling akhir dari list data sebagai sentinel (penjaga). Hal ini memastikan proses pencarian pasti akan menemukan target, sehingga program tidak perlu berulang kali mengecek batas indeks array.
- i = 0 -> Inisialisasi variabel indeks i dengan nilai 0 untuk memulai pencarian dari elemen pertama (awal list).
- Perulangan while data[i] != target: -> Digunakan untuk mengecek kecocokan data. Program akan terus melakukan perulangan selama nilai elemen pada indeks ke-i tidak sama dengan nilai target yang dicari.
- i += 1 -> Menambah nilai penunjuk indeks i untuk mengecek elemen di posisi selanjutnya.
- data.pop() -> Menghapus elemen sentinel yang tadi disisipkan di akhir list, sehingga list kembali ke jumlah dan isi aslinya.
- Pengecekan if i < n: -> Mengevaluasi apakah indeks ditemukannya target (i) berada di dalam rentang jumlah data asli (n).
- Jika nilai i kurang dari n, berarti elemen ditemukan pada data asli, kemudian mengembalikan nilai True beserta posisi indeksnya (i).
- Jika salah (else), berarti target yang cocok adalah sentinel di paling akhir (artinya nama tidak ada di list asli). Program mengembalikan nilai False dan -1.

2. Fungsi main()

- Bertugas sebagai program utama untuk mendeklarasikan kumpulan data, mengelola interaksi dengan pengguna (input/output), dan mengeksekusi logika pencarian.
- Mendeklarasikan variabel list bernama data yang sudah berisikan hardcoded daftar nama-nama mahasiswa.
- n = len(data) -> Menyimpan total jumlah elemen (panjang list) data mahasiswa ke dalam variabel n.
- print(f"Data array: {data}") -> Menampilkan keseluruhan isi daftar nama mahasiswa ke layar sebelum proses pencarian dilakukan.

3. Input Data Target Pencarian:

- Menggunakan Nested Loop while True yang diiringi blok try-except untuk meminta pengguna memasukkan nama mahasiswa yang ingin dicari (target). Tujuannya untuk menangani potensi error. Apabila terdapat kesalahan format value, program akan menangkap exception, menampilkan pesan "Input tidak valid, silakan masukkan ulang", dan terus mengulang permintaan input tanpa menyebabkan program crash. Perulangan akan dihentikan (break) jika input berhasil diterima.

4. Pemanggilan Fungsi:

- found, index = sequential_search_sentinel(data, n, target) -> Mengeksekusi fungsi pencarian dengan memberikan list data, panjang list n, dan nama target. Hasil dari fungsi berupa tuple (boolean dan angka) akan di-unpack ke dalam variabel found dan index.

5. Proses & Output:

- Menggunakan percabangan if found: untuk menentukan output yang akan dicetak.
- Jika found bernilai True, program menampilkan output yang menginformasikan bahwa nama berhasil ditemukan, dilengkapi dengan letak indeks (dimulai dari 0) dan letak urutan elemennya (indeks + 1).
- Jika found bernilai False (masuk ke blok else), program menampilkan output peringatan bahwa nama yang dicari tidak ditemukan di dalam sekumpulan data tersebut.

## d. Output Program

<img width="1307" height="129" alt="image" src="https://github.com/user-attachments/assets/5481273e-a4e3-4e1f-8711-d0d8bb6a31e4" />

1. Tampilan Data Awal

- Saat program pertama kali dijalankan, program akan langsung mencetak keseluruhan isi daftar (array) yang berisi nama-nama mahasiswa ke layar dengan format awalan Data array: ['Ridho', 'Danish', ...].
Di sini, user bisa melihat secara langsung sekumpulan data yang dijadikan sebagai sumber pencarian.

2. Input Target Pencarian

- Setelah data awal ditampilkan, program akan memunculkan prompt teks "Masukkan Nama Mahasiswa PSTI D yang ingin dicari : " dan menunggu user untuk mengetikkan nama target.
- Program sudah dibekali dengan penanganan error (try-except ValueError). Apabila terjadi error nilai (meskipun secara bawaan input teks selalu diterima sebagai string), program akan memunculkan pesan "Input tidak valid, silakan masukkan ulang" dan terus mengulang permintaan input agar program tidak crash.

3. Tampilan Hasil Pencarian (Jika Data Ditemukan)

- Jika nama yang diketikkan user benar-benar ada dan persis (ingat bahwa pencarian ini sensitif terhadap huruf besar/kecil) dengan data di dalam array, program akan menyatakan pencarian berhasil.
- Program kemudian menampilkan hasil berupa teks "Nama '[nama_target]' ditemukan pada indeks ke-[x] (elemen ke-[y]).", yang memberitahu posisi index (dimulai dari 0) dan urutan elemennya.

4. Tampilan Hasil Pencarian (Jika Data Tidak Ditemukan)

- Jika user memasukkan nama yang tidak terdaftar di dalam array atau terdapat kesalahan pengetikan/huruf kapital, program akan menyatakan bahwa pencarian gagal.
- Program kemudian memunculkan pesan "Nama '[nama_target]' tidak ditemukan.", dan proses eksekusi program selesai.
  
## e. Link Youtube
https://youtu.be/kQpL-u26s7Y
