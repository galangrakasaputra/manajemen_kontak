class ManageKontak:
    def __init__(self):
        self.kontak = []

    def lihat(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}. {item["Nama"]} ({item["HP"]})')
        else:
            print("tidak ada kontak")
            return 1

    def tambah(self):
        nama = input("Masukan Nama Baru : ")
        hp = int(input("Masukan Nomor HP baru : " ))
        kontak_baru = {'Nama': nama, 'HP': hp}
        self.kontak.append(kontak_baru)
        print("berhasil di tambah")

    def hapus(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["Nama"]} ({item["HP"]})')    
        else:
            print("tidak ada kontak")
            return 1
        
        hapus = int(input("Kontak mana yang ingin Dihapus ? "))
        if 0 < hapus <= len(self.kontak):
            del self.kontak[hapus-1]
            print("berhasil dihapus")
        else:
            print("Kontak Tidak ada")
            return 1

    def edit(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["Nama"]} ({item["HP"]})')    
        else:
            print("tidak ada kontak")
            return 1

        edit = int(input("Kontak mana yang ingin diubah ? "))
        
        if 0 < edit <= len(self.kontak):
            namaBaru = input("Masukan Nama Baru : " )
            hpBaru = int(input("Masukan No HP Baru : "))
            ubah_kontak = {'Nama': namaBaru, 'HP': hpBaru}
            print(f'Kontak dengan Nama {self.kontak[edit-1]["Nama"]} diubah menjadi {namaBaru} serta No HP nya dari {self.kontak[edit-1]["HP"]} diubah menjadi {hpBaru}')
            self.kontak[edit-1] = ubah_kontak
            print("Berhasil Ubah Kontak")
        else:
            print("Tidak ada Kontak yang dipilih")
            return 1

kontak_baru = ManageKontak()

while True:
    print("\nMenu")
    print("1. Melihat Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Mengubah Kontak")
    print("5. Selesai")

    pilihan = int(input("Pilih Menu : "))

    if pilihan == 1:
        kontak_baru.lihat()
    elif pilihan == 2:
        kontak_baru.tambah()
    elif pilihan == 3:
        kontak_baru.hapus()
    elif pilihan == 4:
        kontak_baru.edit()
    elif pilihan == 5:
        break
    else:
        print("Pilihan tidak ada")