# ======================================================================
# BAGIAN 1: PERSIAPAN DATA
# ======================================================================

# Data penjualan bulanan untuk setiap produk disimpan dalam bentuk list (vektor).
# Setiap elemen dalam list mewakili penjualan dalam satu bulan.
product_A = [120, 150, 130, 170, 200, 190]
product_B = [80, 100, 90, 110, 130, 120]
product_C = [200, 210, 190, 180, 220, 210]


# ======================================================================
# BAGIAN 2: FUNGSI-FUNGSI UNTUK ANALISIS
# ======================================================================

def total_sales(product):
    """
    Fungsi ini menghitung total penjualan dari sebuah produk.
    Args:
        product (list): Sebuah list berisi angka penjualan bulanan.
    Returns:
        int: Jumlah total penjualan.
    """
    total = 0
    # Melakukan iterasi pada setiap angka penjualan dalam list dan menambahkannya ke total.
    for num in product:
        total += num
    return total


def highest_sales(product):
    """
    Fungsi ini mencari nilai penjualan tertinggi dan bulan terjadinya.
    Args:
        product (list): Sebuah list berisi angka penjualan bulanan.
    Returns:
        tuple: Berisi (nilai penjualan tertinggi, nomor bulan).
    """
    sales_value = 0  # Inisialisasi nilai tertinggi dengan 0.
    month = 0        # Inisialisasi bulan.
    # Menggunakan enumerate untuk mendapatkan indeks (i) dan nilai (num) sekaligus.
    for i, num in enumerate(product):
        # Jika nilai saat ini lebih besar dari nilai tertinggi yang tersimpan.
        if num > sales_value:
            sales_value = num  # Perbarui nilai tertinggi.
            month = i + 1      # Simpan nomor bulannya (indeks + 1).
    return sales_value, month


def lowest_sales(product):
    """
    Fungsi ini mencari nilai penjualan terendah dan bulan terjadinya.
    Args:
        product (list): Sebuah list berisi angka penjualan bulanan.
    Returns:
        tuple: Berisi (nilai penjualan terendah, nomor bulan).
    """
    sales_value = float(
        # Inisialisasi dengan nilai tak terhingga agar angka pertama pasti lebih kecil.
        'inf')
    month = 0
    for i, num in enumerate(product):
        # Jika nilai saat ini lebih kecil dari nilai terendah yang tersimpan.
        if num < sales_value:
            sales_value = num  # Perbarui nilai terendah.
            month = i + 1      # Simpan nomor bulannya.
    return sales_value, month


def average_sales(product):
    """
    Fungsi ini menghitung rata-rata penjualan bulanan.
    Memanfaatkan fungsi total_sales() yang sudah ada.
    """
    # Rata-rata adalah total penjualan dibagi jumlah bulan (panjang list).
    average = total_sales(product) / len(product)
    return average


def get_boom_sales(product):
    """
    Fungsi ini mengidentifikasi penjualan yang dianggap "lonjakan" (boom).
    Lonjakan terjadi jika penjualan suatu bulan melebihi 20% dari rata-rata.
    Args:
        product (list): Sebuah list berisi angka penjualan bulanan.
    Returns:
        tuple: Berisi (list nilai penjualan yang melonjak, list bulan terjadinya lonjakan).
    """
    boom_values = []  # List untuk menyimpan nilai penjualan yang melonjak.
    boom_months = []  # List untuk menyimpan bulan terjadinya lonjakan.
    average = average_sales(product)

    # Menetapkan ambang batas: penjualan dianggap melonjak jika 20% di atas rata-rata.
    threshold_value = average * 1.20

    for index, num in enumerate(product):
        # Memeriksa apakah penjualan bulan ini melampaui ambang batas.
        if num >= threshold_value:
            boom_values.append(num)
            boom_months.append(index + 1)

    return boom_values, boom_months


def format_month(month_number):
    """
    Fungsi bantuan untuk memformat angka bulan menjadi string (1st, 2nd, 3rd, 4th, dst).
    """
    if month_number == 1:
        return f'{month_number}st'
    elif month_number == 2:
        return f'{month_number}nd'
    elif month_number == 3:
        return f'{month_number}rd'
    else:
        return f'{month_number}th'

# ======================================================================
# BAGIAN 3: PEMBUATAN LAPORAN UTAMA
# ======================================================================


# Mengelompokkan semua data produk ke dalam dictionary untuk diproses secara otomatis.
product_data = {
    'Produk A': product_A,
    'Produk B': product_B,
    'Produk C': product_C
}

# Mencetak header laporan.
print('======================================================================')
print('                     LAPORAN ANALISIS PENJUALAN PRODUK                  ')
print('======================================================================')

# Melakukan iterasi untuk setiap produk dalam dictionary product_data.
for name, data in product_data.items():
    # Memanggil fungsi-fungsi analisis untuk mendapatkan data yang dibutuhkan.
    total = total_sales(data)
    high_val, high_month = highest_sales(data)
    low_val, low_month = lowest_sales(data)
    boom_values, boom_months = get_boom_sales(data)

    # Mencetak hasil analisis untuk setiap produk.
    print(f'\n--- DATA PENJUALAN {name.upper()} ---')
    print(f'a. Total Penjualan: {total} unit')
    print(
        f'b. Penjualan Tertinggi: {high_val} unit (pada bulan ke-{format_month(high_month)})')
    print(
        f'   Penjualan Terendah: {low_val} unit (pada bulan ke-{format_month(low_month)})')

    # Memeriksa apakah ada lonjakan penjualan.
    if boom_values:
        # Menggabungkan nilai dan bulan jika ada lebih dari satu lonjakan.
        sales_str = ", ".join(map(str, boom_values))
        months_str = ", ".join(map(format_month, boom_months))
        print(
            f'c. Produk ini mengalami lonjakan penjualan pada bulan ke-{months_str}, yaitu sebesar {sales_str} unit.')
    else:
        print(f'c. Produk ini tidak mengalami lonjakan penjualan yang signifikan.')

# Mencetak footer laporan.
print('======================================================================')
