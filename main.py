test = {'Nama' : "Test", 'HP' : '2938123'}

kontak = [test]
def lihat():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["Nama"]} ({item["HP"]})')
    else:
        print("tidak ada kontak")
        return 1

def tambah():
    nama = input("Masukan Nama Baru : ")
    hp = int(input("Masukan Nomor HP baru : " ))
    kontak_baru = {'Nama': nama, 'HP': hp}
    kontak.append(kontak_baru)
    print("berhasil di tambah")

def hapus():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["Nama"]} ({item["HP"]})')    
    else:
        print("tidak ada kontak")
        return 1
    
    hapus = int(input("Kontak mana yang ingin Dihapus ? "))
    if 0 < hapus <= len(kontak):
        del kontak[hapus-1]
        print("berhasil dihapus")
    else:
        print("Kontak Tidak ada")
        return 1

def edit():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["Nama"]} ({item["HP"]})')    
    else:
        print("tidak ada kontak")
        return 1

    edit = int(input("Kontak mana yang ingin diubah ? "))
    
    if 0 < edit <= len(kontak):
        namaBaru = input("Masukan Nama Baru : " )
        hpBaru = int(input("Masukan No HP Baru : "))
        ubah_kontak = {'Nama': namaBaru, 'HP': hpBaru}
        print(f'Kontak dengan Nama {kontak[edit-1]["Nama"]} diubah menjadi {namaBaru} serta No HP nya dari {kontak[edit-1]["HP"]} diubah menjadi {hpBaru}')
        kontak[edit-1] = ubah_kontak
        print("Berhasil Ubah Kontak")
    else:
        print("Tidak ada Kontak yang dipilih")
        return 1
        
while True:
    print("\nMenu")
    print("1. Melihat Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Mengubah Kontak")
    print("5. Selesai")

    pilihan = int(input("Pilih Menu : "))

    if pilihan == 1:
        lihat()
    elif pilihan == 2:
        tambah()
    elif pilihan == 3:
        hapus()
    elif pilihan == 4:
        edit()
    elif pilihan == 5:
        break
    else:
        print("Pilihan tidak ada")