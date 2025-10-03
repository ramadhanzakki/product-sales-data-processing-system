product_A = [120, 150, 130, 170, 200, 190]
product_B = [80, 100, 90, 110, 130, 120]
product_C = [200, 210, 190, 180, 220, 210]


def total_sales(product):
    total = 0
    for num in product:
        total += num
    return total


def highest_sales(product):
    sales_value = 0
    month = 0 
    for i, num in enumerate(product):
        if num > sales_value: 
            month = i + 1
            sales_value = num
    return sales_value, month


def lowest_sales(product):
    sales_value = float('inf')
    month = 0
    for i, num in enumerate(product):
        if num < sales_value:
            month = i + 1
            sales_value = num
    return sales_value, month


def average_sales(product):
    average = total_sales(product) / len(product)
    return average


def get_boom_sales(product):
    sales = []
    average = average_sales(product)
    threshold = 0.2
    boom_sales = average + (threshold * average)
    for index, num in enumerate(product):
        if num >= boom_sales:
            sales.append(num)
    return sales, index
    

product_data = {
    'produk A': product_A,
    'produk B': product_B,
    'produk C': product_C
}


print('======================================================================')
print('                  LAPORAN ANALISIS PENJUALAN PRODUK                   ')
print('======================================================================')


for name, data in product_data.items():
    total = total_sales(data)
    high_val, high_mounth = highest_sales(data)
    low_val, low_mounth = lowest_sales(data)
    boom_sales, boom_mounth = get_boom_sales(data)

    def mounth(index):
        if index == 1:
            return(f'{index}st')
        elif index == 2:
            return(f'{index}nd')
        else:
            return(f'{index}th')

    print(f'\n--- DATA SALES {name.upper()}---')
    print(f'a. Total sales: {total} unit')
    print(f'b. Highest sales: {high_val} unit (in the {mounth(high_mounth)} mounth)')
    print(f'   Lowest sales: {low_val} unit (in the {mounth(low_mounth)} mounth)')
    if boom_sales:
        sales_str = ", ".join(map(str, boom_sales))
        print(f'c. This product experienced an unusual surge in sales in {mounth(boom_mounth)} with {boom_sales} sales')
    else:
        print(f'c. This product did not experience a significant surge in sales.')

print('======================================================================')