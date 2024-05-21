# Aplikasi Play Store
def aplikasiPlayStore(n):
    # Membuat dictionary berisi Kategori dan Aplikasi
    dictKategori = dict()
    for i in range(n):
        kategori = str(input(f'Masukkan kategori ke {i+1}: '))
        lstAplikasi = []
        for j in range(5):
            aplikasi = str(input(f'Masukkan aplikasi ke {j+1} dari kategori {kategori}: '))
            lstAplikasi.append(aplikasi)
        else:
            dictKategori[kategori] = lstAplikasi
            print()
    print(dictKategori)
    print()
    
    # Membuat List Untuk Menyimpan Aplikasi Dari Dictionary
    listAplikasi = []
    for k in dictKategori.keys():
        listAplikasi.append(dictKategori[k])
    # Aplikasi Yang Terdapat Pada Semua Kategori
    hasil = set(listAplikasi[0])
    for i in range(1, len(listAplikasi)):
        hasil = hasil.intersection(set(listAplikasi[i]))
    if len(hasil) > 0:
        print("Aplikasi Yang Terdapat Pada Semua Kategori:", hasil)
    else:
        print('Tidak Ada Aplikasi Yang Muncul Pada Semua Kategori!')
    # Aplikasi Yang Muncul Hanya Pada Satu Kategori (fitur tambahan 1)
    hasil1 = set(listAplikasi[0])
    for i in range(1, len(listAplikasi)):
        hasil1 = hasil1.symmetric_difference((set(listAplikasi[i])))
    if len(hasil1) > 0:
        print("Aplikasi Yang Muncul Hanya Pada Satu Kategori:", hasil1)
    else:
        print('Semua Aplikasi Muncul Pada Semua Kategori!')
    # Aplikasi Yang Muncul Tepat 2 Kategori (fitur tambahan 2)
    if n > 2:
        dictAplikasi = {}
        for lst in listAplikasi:
            for aplikasi in lst:
                if aplikasi in dictAplikasi:
                    dictAplikasi[aplikasi] += 1
                else:
                    dictAplikasi[aplikasi] = 1
        hasil2 = set([k for k, v in dictAplikasi.items() if v == 2])
        if hasil2:
            print('Aplikasi Yang Muncul Tepat 2 Kategori:', hasil2)
        else:
            print('Tidak ada aplikasi yang muncul tepat 2 kategori!')
    
n = int(input('Masukkan berapa kategori: '))
aplikasiPlayStore(n)