n = int(input("Masukkan jumlah kategori: "))

apps = {}
for i in range(n):
    kategori = str(input(f"Masukkan nama kategori ke-{i+1}: "))
    set_apps = set()
    for j in range(5):
        app = str(input(f"Masukkan nama aplikasi ke-{j+1}: "))
        set_apps.add(app)
    apps[kategori] = set_apps
    
list_kategori = []
for kategori in apps:
    list_kategori.append(kategori[kategori]) 
    
hasil = list_kategori[0]
for i in range(1, len(list_kategori)):
    hasil = hasil.intersection(list_kategori[i])
    
print(apps)