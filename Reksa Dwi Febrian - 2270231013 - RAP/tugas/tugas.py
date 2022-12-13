import sys
total = []

print("------Reksa Dwi Febrian---------")
print("----Warnet Reksa Dwi Febrian----")
print("----------2270231013------------")

nama = input("Nama Pelanggan : ")
tanggal = input("Tanggal Transaksi : ")
alamat = print(" Jatiwaringin,Pondok Gede, RT.009/RW.005, Jaticempaka, Kec. Pd. Gede, Kota Bks, Jawa Barat 16969")
notelp = print("+62 8912462355")

def daftar_barang():
    print("________________________________________________")
    print(" No   |  biling warnet reksa dwi febrian  | Harga")
    print("ALAMAT|  Jatiwaringin,Pondok Gede RT001/002 NO 50")
    print("________________________________________________")
    print(" -1-  | Play Station 2                    | 3000")
    print(" -2-  | Play Station 3                    | 6000")
    print(" -3-  | Play Station 4                    | 8000")
    print(" -4-  | KOMPUTER                          | 10000")
    print(" -5-  | Laptop                            | 9000")
    print("________________________________________________")
    kode = int(input("Masukkan pilihan yang ingin di pilih  : "))
    if kode == 1:
        jumlah1 = int(input("Lama Rental : "))
        total1 = 3000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Lama Rental : "))
        total2 = 6000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Lama Rental : "))
        total3 = 8000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Lama Rental : "))
        total4 = 10000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Lama Rental : "))
        total5 = 9000 * jumlah5 
        barang = "Laptop"  
        total.append(total5)
        tanya()
    return
    
def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah biling? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":

        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")



def akhir():
    for harga in total:
        print("total pembayaran         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 14999:
            diskon = a * 10/100
        elif a > 29999:
            diskon = a * 10/100
        elif a > 39999:
            diskon = a * 10/100
        elif a > 49999:
            diskon = a * 10/100
        elif a > 44999:
            diskon = a * 10/100
        else:
            diskon = 0
        print("Potongan Harga          : ", diskon)
        totalakhir = a - diskon
        print("Total                   : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")
    return
daftar_barang()