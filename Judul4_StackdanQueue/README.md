#  Mencari Nama Mahasiswa (sequential search sentinel)

## a. Judul Program
Mencari Nama Mahasiswa Menggunakan sequential search sentinel

## b. Deskripsi Singkat
Program ini dirancang untuk melakukan pencarian data nama mahasiswa dari program studi PSTI D di dalam sebuah kumpulan data (array) yang telah ditentukan, dengan memanfaatkan algoritma Sequential Search berbasis Sentinel. Sistem ini beroperasi secara efisien dengan cara menambahkan elemen target yang ingin dicari ke posisi paling akhir dari array sebagai "sentinel" (penjaga). Penambahan sentinel ini memungkinkan proses perulangan berjalan lebih cepat karena mengeliminasi kebutuhan untuk terus-menerus memeriksa batas indeks array pada setiap langkah evaluasi. Setelah proses pencarian berhenti pada elemen yang cocok, program kemudian membuang sentinel tersebut dan mengevaluasi apakah indeks kecocokan berada di dalam rentang data asli untuk menyimpulkan apakah nama tersebut benar-benar ditemukan atau tidak. Selain itu, program ini juga mengimplementasikan mekanisme exception handling menggunakan blok try-except pada saat menerima masukan dari pengguna untuk menangani potensi error, sehingga program dapat memberikan peringatan untuk mengulang kembali jika masukan dianggap tidak valid.

