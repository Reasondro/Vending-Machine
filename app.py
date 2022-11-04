# Sebelum menjalankan program, harap ketik line berikut di terminal Anda:
# pip install -r requirements.txt
# Dibutuhkan untuk menginstall kebutuhan tertentu dari virtual enviroment yang dibuat ("plsworkvenv")
from playsound import playsound

items = [
    {
        'Kode': 1,
        'Nama': 'Aqua',
        'Harga': 10000},
    {
        'Kode': 2,
        'Nama': 'Pocari',
        'Harga': 15000},
    {
        'Kode': 3,
        'Nama': 'Teh Pucuk',
        'Harga': 10000},
    {
        'Kode': 4,
        'Nama': 'Yogurt',
        'Harga': 15000},
    {
        'Kode': 5,
        'Nama': 'Sprite',
        'Harga': 10000},
    {
        'Kode': 6,
        'Nama': 'Fanta',
        'Harga': 10000},
    {
        'Kode': 7,
        'Nama': 'Coca-cola',
        'Harga': 10000},
    {
        'Kode': 8,
        'Nama': 'Milo',
        'Harga': 20000},
    {
        'Kode': 9,
        'Nama': 'Starbucks',
        'Harga': 30000},
]

keluar = False
item = ''

while keluar == False:
    print(f"Welcome to 7's vending machine")
    for i in items:
        print(f"Nama item : {i['Nama']}\tHarga: {i['Harga']}\tKode: {i['Kode']}")

    query = int(input("Masukkan nomor kode minuman yang ingin Anda beli: "))
    playsound('beep3.wav')
    for i in items:
        if query == i['Kode']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Baik, {item['Nama']} akan mengenakan Anda biaya sebesar {item['Harga']} rupiah")

        price = int(input(f"Masukkan {item['Harga']} rupiah untuk membeli: "))
        playsound('beep3.wav')
        kembalian = price - item['Harga']
        if price == item['Harga']:
            playsound('vending2.wav')
            print(f"Terima kasih untuk membeli, berikut {item['Nama']} Anda.")

        elif price > item['Harga']:
            playsound('vending2.wav')
            print(f"Berikut kembalian dan minuman pembelian Anda {item['Nama']}", kembalian)
        elif price < item['Harga']:
            print(f"Uang yang Anda masukkan tidak cukup untuk membeli {item['Nama']}.")

    query = input("Untuk mengakhiri pembeilan tekan q, jika ingin melanjutkan tekan c: ")
    playsound('beep3.wav')
    if query == 'c':
        keluar = False
    else:
        keluar = True
    print('')   
