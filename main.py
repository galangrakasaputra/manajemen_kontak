test = {'Nama' : "Test", 'HP' : '2938123'}

kontak = [test]
while True:
    print("\nMenu")
    print("1. Melihat Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("5. Selesai")

    pilihan = int(input("Pilih Menu : "))

    if pilihan == 1:
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["Nama"]} ({item["HP"]})')
        else:
            print("tidak ada kontak")
    elif pilihan == 2:
        nama = input("Masukan Nama Baru : ")
        hp = int(input("Masukan Nomor HP baru : " ))
        kontak_baru = {'Nama': nama, 'HP': hp}
        kontak.append(kontak_baru)
        print("berhasil di tambah")
    elif pilihan == 3:
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["Nama"]} ({item["HP"]})')    
        else:
            print("tidak ada kontak")
            continue
        
        hapus = int(input("Kontak mana yang ingin Dihapus ? "))
        del kontak[hapus-1]
        print("berhasil dihapus")
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak ada")