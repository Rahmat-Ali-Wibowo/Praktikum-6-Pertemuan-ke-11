# Inisialisasi dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    data_mahasiswa[nama] = {
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    }
    print(f"Data untuk {nama} telah ditambahkan.")

def tampilkan():
    if data_mahasiswa:
        print("\nDaftar Data Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"Nama: {nama}, Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Nilai Akhir: {nilai['nilai_akhir']:.2f}")
    else:
        print("Tidak ada data mahasiswa.")

def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data untuk {nama} telah dihapus.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

def ubah(nama):
    if nama in data_mahasiswa:
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        
        nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
        data_mahasiswa[nama] = {
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'nilai_akhir': nilai_akhir
        }
        print(f"Data untuk {nama} telah diperbarui.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

def menu():
    while True:
        print("\nMenu Pilihan:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang datanya akan dihapus: ")
            hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang datanya akan diubah: ")
            ubah(nama)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan menu
menu()
