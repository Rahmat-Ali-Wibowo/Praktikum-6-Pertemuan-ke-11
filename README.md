# Program Mengelola Daftar Nilai Mahasiswa

## Deskripsi
Program ini memungkinkan pengguna untuk mengelola daftar nilai mahasiswa menggunakan dictionary. Pengguna dapat menambah, mengubah, menghapus, dan menampilkan data mahasiswa. Nilai akhir dihitung berdasarkan komponen nilai tugas, UTS, dan UAS.

## Flowchart

```plaintext
+------------------------------------------------------+
| Mulai                                                 |
+------------------------------------------------------+
          |
          v
+----------------------------+
| Inisialisasi dictionary    |
| data_mahasiswa             |
+----------------------------+
          |
          v
+----------------------------+
| Tampilkan menu pilihan     |
| (Tambah, Tampilkan, Hapus, |
| Ubah, Keluar)              |
+----------------------------+
          |
          v
+----------------------------+
| Input pilihan pengguna     |
| (1/2/3/4/5)                |
+----------------------------+
          |
          v
+-----------------------------+
| Apakah pilihan '1'?         |
| (Tambah Data)               |
+-------------+---------------+
              |Tidak                       |Ya
              v                            v
+-------------+-------------+  +-----------+-----------+
| Lanjutkan ke pilihan lain |  | Input nama, tugas, UTS,|
| (2/3/4/5)                 |  | UAS                   |
+-------------+-------------+  +-----------------------+
                               | Hitung nilai akhir    |
                               | Tambah data ke list   |
                               +-----------------------+
                                         |
                                         v
+-----------------------------+ +-----------------------+
| Apakah pilihan '2'?         | | Apakah pilihan '3'?   |
| (Tampilkan Data)            | | (Hapus Data)          |
+-------------+---------------+ +-------------+---------+
              |Tidak                      |Ya
              v                           v
+-------------+-------------+  +----------+-----------+
| Lanjutkan ke pilihan lain |  | Input nama mahasiswa  |
| (3/4/5)                   |  | Jika ditemukan,       |
+-------------+-------------+  | hapus data            |
                               +-----------------------+
                                         |
                                         v
+-----------------------------+ +-----------------------+
| Apakah pilihan '4'?         | | Apakah pilihan '5'?   |
| (Ubah Data)                 | | (Keluar)              |
+-------------+---------------+ +-------------+---------+
              |Tidak                      |Ya
              v                           v
+-------------+-------------+  +-----------+-----------+
| Lanjutkan ke pilihan lain |  | Keluar dari program    |
| (5)                       |  +-----------------------+
+-------------+-------------+
