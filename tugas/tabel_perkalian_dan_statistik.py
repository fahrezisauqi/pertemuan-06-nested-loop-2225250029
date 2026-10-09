
# Tugas 3: Tabel Perkalian dan Statistik
# Pertemuan 6 - Nested Loop Python

print("Tabel Perkalian dan Statistik")

n = int(input("Masukkan n positif: "))

# Validasi input agar n harus positif.
while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n positif: "))

# Akumulator dan counter untuk seluruh tabel.
total_semua = 0
count_genap = 0

# Loop luar mengatur baris.
for i in range(1, n + 1):
    total_baris = 0

    # Loop dalam mengatur kolom.
    for j in range(1, n + 1):
        hasil = i * j

        # Menampilkan hasil perkalian.
        print(f"{hasil:4}", end="")

        # Menghitung jumlah pada setiap baris.
        total_baris += hasil

        # Menghitung jumlah keseluruhan.
        total_semua += hasil

        # Menghitung banyak hasil yang genap.
        if hasil % 2 == 0:
            count_genap += 1

    # Dijalankan setelah satu baris selesai.
    print(f"   | jumlah baris = {total_baris}")

# Statistik keseluruhan.
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
