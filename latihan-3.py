def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            text = file.read()
            return text.lower().split()
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    except PermissionError:
        print(f"Tidak dapat membaca file '{nama_file}'.")

def main():
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")

    kata1 = baca_file(file1)
    kata2 = baca_file(file2)

    if kata1 and kata2:
        common_words = set(kata1) & set(kata2)
        print("Kata-kata yang muncul pada kedua file:")
        for word in common_words:
            print(word)

if __name__ == "__main__":
    main()