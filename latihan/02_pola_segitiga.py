
# Latihan 2: Pola Segitiga
# Loop luar menentukan baris.
# Loop dalam menentukan jumlah bintang.

n = int(input("Masukkan n positif: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n positif: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
