# Studi Kasus: Analisis Data Penjualan Produk

Repositori ini berisi skrip Python sederhana yang dibuat untuk menyelesaikan studi kasus mengenai pengolahan dan analisis data penjualan produk. Skrip ini melakukan analisis dasar untuk mengevaluasi kinerja produk berdasarkan data penjualan bulanan.

##  Deskripsi Kasus

Seorang analis data di perusahaan retail ditugaskan untuk menganalisis data penjualan beberapa produk baru. Tujuannya adalah untuk menentukan kinerja produk, menemukan bulan dengan performa terbaik dan terburuk, serta mengidentifikasi adanya lonjakan penjualan yang tidak biasa. Data penjualan disediakan dalam bentuk matriks (list) di mana setiap baris mewakili produk dan setiap kolom mewakili bulan.

## Fungsionalitas Utama

Skrip ini memiliki beberapa fungsi utama untuk menjawab permintaan analisis:

-   **Total Penjualan**: Menghitung total unit yang terjual untuk setiap produk selama periode 6 bulan.
-   **Kinerja Bulanan**: Menemukan nilai penjualan **tertinggi** dan **terendah** serta mengidentifikasi **bulan** terjadinya.
-   **Identifikasi Lonjakan Penjualan**: Mendeteksi "boom sales" atau lonjakan penjualan yang tidak biasa. Sebuah penjualan dianggap sebagai lonjakan jika nilainya **20% lebih tinggi** dari rata-rata penjualan bulanan produk tersebut.
-   **Laporan Otomatis**: Menghasilkan laporan ringkas yang menampilkan semua hasil analisis secara terstruktur untuk setiap produk langsung di terminal.

## Teknologi yang Digunakan

-   **Python 3**: Seluruh logika analisis dibuat menggunakan Python murni tanpa ketergantungan pada library eksternal.

## Cara Menjalankan Skrip

Untuk menjalankan analisis, ikuti langkah-langkah berikut:

1.  **Clone repositori ini:**
    ```bash
    git clone [URL_REPOSITORI_ANDA]
    ```
2.  **Masuk ke direktori proyek:**
    ```bash
    cd [NAMA_DIREKTORI_ANDA]
    ```
3.  **Jalankan file Python:**
    (Pastikan Anda menamai file Anda, misalnya `analisis_penjualan.py`)
    ```bash
    python analisis_penjualan.py
    ```
4.  Hasil analisis akan langsung ditampilkan di terminal Anda.

## Contoh Output

```text
======================================================================
                     LAPORAN ANALISIS PENJUALAN PRODUK                  
======================================================================

--- DATA PENJUALAN PRODUK A ---
a. Total Penjualan: 960 unit
b. Penjualan Tertinggi: 200 unit (pada bulan ke-5th)
   Penjualan Terendah: 120 unit (pada bulan ke-1st)
c. Produk ini mengalami lonjakan penjualan pada bulan ke-5th, yaitu sebesar 200 unit.

--- DATA PENJUALAN PRODUK B ---
a. Total Penjualan: 630 unit
b. Penjualan Tertinggi: 130 unit (pada bulan ke-5th)
   Penjualan Terendah: 80 unit (pada bulan ke-1st)
c. Produk ini tidak mengalami lonjakan penjualan yang signifikan.

--- DATA PENJUALAN PRODUK C ---
a. Total Penjualan: 1210 unit
b. Penjualan Tertinggi: 220 unit (pada bulan ke-5th)
   Penjualan Terendah: 180 unit (pada bulan ke-4th)
c. Produk ini mengalami lonjakan penjualan pada bulan ke-5th, yaitu sebesar 220 unit.
======================================================================
