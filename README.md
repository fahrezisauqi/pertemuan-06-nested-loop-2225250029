# 🐍 Pertemuan 06 — Nested Loop Python

<p align="center">
  <b>Algoritma dan Pemrograman</b><br>
  Program Studi S1 Pendidikan Matematika<br>
  FKIP — Universitas Sultan Ageng Tirtayasa
</p>

---

## 📌 Deskripsi Proyek

Repositori ini berisi latihan dan tugas pemrograman Python pada Pertemuan 6 dengan materi **Nested Loop, Pola, Akumulasi, dan Pencacahan**.

Proyek ini dibuat untuk memahami penggunaan perulangan bersarang dalam memproses data, membentuk pola, menghitung jumlah, dan mencacah hasil berdasarkan kondisi tertentu.

## 👨‍🎓 Identitas Mahasiswa

| Keterangan | Data |
|---|---|
| Nama | Fahrezi Sauqi Alghani|
| NIM | 2225250029 |
| Kelas | 3E|
| Mata Kuliah | Algoritma dan Pemrograman |
| Pertemuan | 06 |

## 🎯 Tujuan Pembelajaran

- Memahami cara kerja nested loop.
- Membentuk pola menggunakan perulangan.
- Menghitung akumulasi nilai per baris dan keseluruhan.
- Menghitung banyak pasangan berdasarkan kondisi.
- Menguji dan menjalankan program Python melalui VS Code.
- Mengelola proyek menggunakan Git dan GitHub.

## 📂 Struktur Proyek

```text
pertemuan-06-nested-loop-NIM/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
│
└── tugas/
    └── tabel_perkalian_dan_statistik.py
```

## 💻 Daftar Latihan

| No. | Nama Program | Deskripsi |
|---|---|---|
| 01 | Pasangan Indeks | Menampilkan pasangan nilai `i` dan `j`. |
| 02 | Pola Segitiga | Membentuk pola bintang berdasarkan input. |
| 03 | Jumlah per Baris | Menghitung jumlah hasil perkalian setiap baris. |
| 04 | Hitung Pasangan | Menghitung pasangan yang memenuhi kondisi `i + j <= n`. |

## 📝 Tugas 3 — Tabel Perkalian dan Statistik

Program utama membuat tabel perkalian berukuran `n × n` dan menghitung statistik dari hasil perkalian.

**Fitur program:**
- Memvalidasi input agar `n` merupakan bilangan bulat positif.
- Menampilkan tabel perkalian dari 1 sampai `n`.
- Menghitung jumlah hasil perkalian pada setiap baris.
- Menghitung total seluruh hasil perkalian.
- Menghitung banyak hasil perkalian yang genap.

## ▶️ Cara Menjalankan Program

Pastikan Python sudah terpasang dan folder proyek telah dibuka di VS Code.

Jalankan salah satu perintah berikut melalui terminal:

```powershell
python latihan/01_pasangan_indeks.py
```

```powershell
python latihan/02_pola_segitiga.py
```

```powershell
python latihan/03_jumlah_per_baris.py
```

```powershell
python latihan/04_hitung_pasangan.py
```

Untuk menjalankan tugas utama:

```powershell
python tugas/tabel_perkalian_dan_statistik.py
```

## 🧪 Hasil Pengujian Tugas 3

| Input `n` | Total Seluruh Hasil | Banyak Hasil Genap |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 9 | 3 |
| 3 | 36 | 5 |

Seluruh nilai di atas merupakan hasil yang diharapkan berdasarkan perhitungan tabel perkalian untuk masing-masing input.

## 🧠 Analisis Algoritma

**1. Nested Loop**

Loop luar mengatur baris, sedangkan loop dalam mengatur kolom. Untuk setiap nilai `i`, loop `j` dijalankan dari awal hingga `n`.

**2. Akumulasi**

Variabel `total_baris` diinisialisasi ulang pada awal setiap baris. Variabel `total_semua` diinisialisasi sebelum kedua loop agar dapat menghitung seluruh hasil perkalian.

**3. Pencacahan**

Variabel `count_genap` bertambah satu setiap kali hasil perkalian memenuhi kondisi `hasil % 2 == 0`.

**4. Efisiensi**

Untuk input `n`, badan loop dalam dijalankan sebanyak `n × n` kali. Kompleksitas waktu program adalah **O(n²)**.

## 📚 Refleksi

Melalui latihan ini, saya mempelajari bahwa posisi dan indentasi perulangan menentukan hasil program. Inisialisasi akumulator harus disesuaikan dengan tujuan perhitungan, sedangkan counter hanya bertambah ketika kondisi yang ditentukan terpenuhi.

Pengujian dengan beberapa nilai input membantu memastikan bahwa hasil program sesuai dengan perhitungan yang diharapkan.

## 🛠️ Teknologi yang Digunakan

- Python 3
- Visual Studio Code
- Git
- GitHub

---

<p align="center">
  <b>Algoritma dan Pemrograman — Pertemuan 06</b><br>
  Universitas Sultan Ageng Tirtayasa
</p>
