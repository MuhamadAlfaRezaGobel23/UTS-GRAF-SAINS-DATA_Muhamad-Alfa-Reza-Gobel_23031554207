# UTS-GRAF-SAINS-DATA_Muhamad-Alfa-Reza-Gobel_23031554207

# UTS Graf Sains Data

Repository ini berisi kumpulan file proyek Ujian Tengah Semester (UTS) mata kuliah Graf Sains Data. Proyek mencakup pengolahan dataset, implementasi Python, penggunaan Neo4j, serta analisis graf berdasarkan data interaksi pengguna dan item dari dataset RetailRocket.

## Struktur Repository

| File | Deskripsi |
|---|---|
| `README.md` | Dokumentasi repository yang menjelaskan tujuan proyek dan fungsi setiap file. |
| `Jawaban Tahapan Pendahuluan.txt` | Berisi jawaban dan penjelasan untuk tahapan pendahuluan pengerjaan UTS Graf Sains Data. |
| `Muhamad Alfa Reza Gobel_207_UTS GSD.ipynb` | Notebook Jupyter yang digunakan untuk menjalankan kode, melakukan analisis data, dan mendokumentasikan tahapan pengerjaan UTS. |
| `P(1)_training.csv` | Dataset training yang digunakan sebagai data utama untuk proses pengolahan dan analisis. |
| `P(2)_testing.csv` | Dataset testing yang digunakan untuk pengujian atau analisis lanjutan sesuai tahapan pengerjaan. |
| `import_retailrocket.py` | Skrip Python untuk mengimpor dataset RetailRocket ke dalam database Neo4j. |
| `main.py` | Skrip utama Python untuk menjalankan proses pengolahan atau analisis graf. |
| `neo4j_query_table_data_Tahap 7.csv` | File CSV yang menyimpan hasil query atau data tabel dari Neo4j pada Tahap 7. |
| `requirements.txt` | Daftar library Python yang diperlukan untuk menjalankan proyek. |

## Teknologi yang Digunakan

- **Python** — pengolahan data dan implementasi analisis.
- **Jupyter Notebook** — menjalankan kode dan mendokumentasikan proses analisis.
- **Neo4j** — database graf untuk menyimpan dan mengelola hubungan antarentitas.
- **NetworkX** — pemodelan dan analisis struktur graf.
- **Pandas** — pengolahan data tabular.
- **Matplotlib** — visualisasi data dan graf.

## Dataset

Proyek ini menggunakan dataset RetailRocket yang berkaitan dengan interaksi pengguna terhadap item. Data tersebut dapat digunakan untuk membentuk graf yang merepresentasikan hubungan antara pengguna dan item berdasarkan aktivitas interaksi.

## Cara Menjalankan

1. Clone repository ini ke komputer lokal.
2. Siapkan lingkungan Python dan instal library yang tercantum dalam `requirements.txt`.
3. Siapkan database Neo4j beserta konfigurasi koneksi yang sesuai.
4. Jalankan notebook atau skrip Python sesuai tahapan pengerjaan.
5. Pastikan file dataset tersedia pada lokasi yang sesuai dengan path yang digunakan dalam kode.

Instalasi library dapat dilakukan dengan perintah:

```bash
pip install -r requirements.txt
```

## Catatan

Pastikan konfigurasi koneksi Neo4j, lokasi dataset, dan dependensi Python telah disesuaikan dengan lingkungan yang digunakan sebelum menjalankan program.
