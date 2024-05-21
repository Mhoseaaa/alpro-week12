def aplikasiPlayStore(n):
    # Membuat dictionary untuk menyimpan kategori dan aplikasinya
    kategoriDict = {}
    for i in range(n):
        kategori = str(input(f'Masukkan nama kategori ke-{i + 1}: '))
        aplikasiList = []
        for j in range(5):
            aplikasi = str(input(f'Masukkan nama aplikasi ke-{j + 1} dalam kategori {kategori}: '))
            aplikasiList.append(aplikasi)
        kategoriDict[kategori] = aplikasiList
        print()

    print(kategoriDict)
    print()

    # Membuat list untuk menyimpan aplikasi dari setiap kategori
    semuaAplikasi = []
    for k in kategoriDict.keys():
        semuaAplikasi.append(kategoriDict[k])

    # Mencari aplikasi yang muncul di semua kategori
    hasil = set(semuaAplikasi[0])
    for i in range(1, len(semuaAplikasi)):
        hasil = hasil.intersection(set(semuaAplikasi[i]))
    if hasil:
        print("Aplikasi yang ada di semua kategori:", hasil)
    else:
        print('Tidak ada aplikasi yang muncul di semua kategori!')

    # Mencari aplikasi yang hanya ada di satu kategori
    unikHasil = set(semuaAplikasi[0])
    for i in range(1, len(semuaAplikasi)):
        unikHasil = unikHasil.symmetric_difference(set(semuaAplikasi[i]))
    if unikHasil:
        print("Aplikasi yang hanya ada di satu kategori:", unikHasil)
    else:
        print('Semua aplikasi muncul di lebih dari satu kategori!')

    # Mencari aplikasi yang muncul tepat di dua kategori
    if n > 2:
        aplikasiCounter = {}
        for lst in semuaAplikasi:
            for aplikasi in lst:
                if aplikasi in aplikasiCounter:
                    aplikasiCounter[aplikasi] += 1
                else:
                    aplikasiCounter[aplikasi] = 1
        duaKategoriHasil = {app for app, count in aplikasiCounter.items() if count == 2}
        if duaKategoriHasil:
            print('Aplikasi yang muncul tepat di dua kategori:', duaKategoriHasil)
        else:
            print('Tidak ada aplikasi yang muncul tepat di dua kategori!')

# Meminta input jumlah kategori dari pengguna
n = int(input('Masukkan jumlah kategori: '))
aplikasiPlayStore(n)