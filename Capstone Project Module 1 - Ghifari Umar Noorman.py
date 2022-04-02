dict_penjualan =  {"A1" : {"Item" : "Broom", "Price" : "10000", "Sold" : "3", "Person in Responsible" : "Ghifari"},
             "A2" : {"Item" : "Chair", "Price" : "50000", "Sold" : "4", "Person in Responsible" : "Umar"}}
dict_baru = {}
def menu_utama():
    status=True
    while status:
        print("--- Main Menu ---")
        print("1. Print Sales Data")
        print("2. Add Sales Data")
        print("3. Update Sales Data")
        print("4. Remove Sales Data")
        print("5. Exit Application")
        pil_menu=input("Insert Menu's Option(1-5): ")
        if pil_menu=="1":
            status=False
            daftar_brg()
        elif pil_menu=="2":
            status=False
            tambah_brg()
        elif pil_menu=="3":
            status=False
            ubah_brg()
        elif pil_menu=="4":
            status=False
            hapus_brg()
        elif pil_menu=="5":
            status=False
            keluar()
def daftar_brg():
    status=True
    while status:
        print("1. All Sales Data")
        print("2. Insert Item's Code")
        print("3. Return to Main Menu")
        pil_daftar=input("Insert Menu's Option(1-3): ")
        if pil_daftar =="1":
            status=False
            all_brg()
        elif pil_daftar=="2":
            status=False
            kode_brg()
        elif pil_daftar=="3":
            status=False
            menu_utama()
def all_brg():
    if len(dict_penjualan)==0:
        print("---No Sales Data---")
        daftar_brg()
    else:
        for i in dict_penjualan:
            print("---Item's Code : {}, Item : {}, Price : {}, Sold : {}, Person in Responsible : {}---".format(i,dict_penjualan[i]["Item"], dict_penjualan[i]["Price"], dict_penjualan[i]["Sold"], dict_penjualan[i]["Person in Responsible"]) )
        daftar_brg()
def kode_brg():
    kode=input("Insert Item's Code: ").capitalize()
    if kode not in dict_penjualan:
        print("---No Sales Data---")
        daftar_brg()
    else:
        print("---Item's Code : {}, Item : {}, Price : {}, Sold : {}, Person in Responsible : {}---".format(kode,dict_penjualan[kode]["Item"], dict_penjualan[kode]["Price"], dict_penjualan[kode]["Sold"], dict_penjualan[kode]["Person in Responsible"]) )
        daftar_brg()
def tambah_brg():
    status=True
    while status:
        print("1. Add Sales Data")
        print("2. Return to Main Menu")
        pil_tambah=input("Insert Option(1-2): ")
        if pil_tambah=="1":
            status=False
            input_brg()
        if pil_tambah=="2":
            status=False
            menu_utama()
def input_brg():
    status=True
    kode=input("Insert Item's Code: ").capitalize()
    if kode not in dict_penjualan:
        nama_brg=input("Insert Item's Name: ").capitalize()
        dict_baru["Item"] = nama_brg
        harga=input("Insert Item's Price: ").capitalize()
        dict_baru["Price"] = harga
        terjual=input("Insert the number of Item's Sold: ").capitalize()
        dict_baru["Sold"] = terjual
        nama=input("Insert Person in Responsible: ").capitalize()
        dict_baru["Person in Responsible"] = nama
        while status:
            tanya_tambah=input("Do you want to save the sales data(Y/N)? ").capitalize()
            if tanya_tambah=="Y":
                status=False
                dict_penjualan[kode]=dict_baru
                print(dict_baru)
                print("---Sales Data Saved---")
                tambah_brg()
            elif tanya_tambah=="N":
                status=False
                print("---Sales Data not Saved---")
                tambah_brg()
    elif kode in dict_penjualan:
        print("---Sales data already exist---")
        tambah_brg()
def ubah_brg():
    status=True
    while status:
        print("1. Update Sales Data")
        print("2. Return to Main Menu")
        pil_ubah=input("Insert Option(1-2): ")
        if pil_ubah=="1":
            status=False
            global kode
            kode=input("Insert Item's Code: ").capitalize()
            if kode in dict_penjualan:
                status=True
                print("Item's Code : {}, Item : {}, Price : {}, Sold : {}, Person in Responsible : {}".format(kode,dict_penjualan[kode]["Item"], dict_penjualan[kode]["Price"], dict_penjualan[kode]["Sold"], dict_penjualan[kode]["Person in Responsible"]))
                while status:
                    pil_ubah3=input("Do you want to update the sales data(Y/N)? ").capitalize()
                    if pil_ubah3=="Y":
                        status=False
                        ganti_key()
                        ubah_brg()
                    elif pil_ubah3=="N":
                        status=False
                        ubah_brg()
            elif kode not in dict_penjualan:
                print("---Sales data doesn't exist---")
                ubah_brg()
        elif pil_ubah=="2":
            status=False
            menu_utama()
def ganti_key():
    key_baru = input("Insert the description you want to change: ")
    key_baru=key_baru.title()
    if key_baru in dict_penjualan[kode]:
        ket_baru = input("Insert the new {} : ".format(key_baru)).capitalize()
        status=True
        while status:
            pil_yn = input("Do you want to update the sales data (Y/N)? ").capitalize()
            if pil_yn == 'Y':
                dict_penjualan[kode][key_baru] = ket_baru
                print("---Sales Data Updated---")
                status=False
            elif pil_yn== 'N':
                print("---Sales Data's not Updated---")
                status=False
    else:
        print("The Description doesn't exist")
        ganti_key()

def hapus_brg():
    status=True
    while status:
        print("1. Remove Sales Data")
        print("2. Return to Main Menu")
        pil_hapus=input("Insert Option(1-2): ")
        if pil_hapus=="1":
            status=False
            delete_brg()
        if pil_hapus=="2":
            status=False
            menu_utama()

def delete_brg():
    kode=input("Insert Item's Code: ").capitalize()
    if kode in dict_penjualan:
        status=True
        while status:
            tanya_hapus=input("Do you want to remove the sales data(Y/N)? ").capitalize()
            if tanya_hapus=="Y":
                status=False
                dict_penjualan.pop(kode)
                print("---Sales Data Removed---")
                hapus_brg()
            elif tanya_hapus=="N":
                status=False
                print("---Sales Data's not Removed---")
                hapus_brg()
    elif kode not in dict_penjualan:
        print("---No Sales Data---")
        hapus_brg()
def keluar():
    print("---Thank You for Visiting---")
menu_utama()
