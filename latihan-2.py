# List menjadi Set
list_data = input("Masukkan data dalam list (pisahkan dengan koma): ").split(",")
set_data = set(list_data)

print("List sebelum konversi:", list_data)
print("Set setelah konversi:", set_data)

# Set menjadi List
set_data = input("Masukkan data dalam set (pisahkan dengan koma): ").split(",")
list_data = list(set_data)

print("Set sebelum konversi:", set_data)
print("List setelah konversi:", list_data)

# Tuple menjadi Set
tuple_data = tuple(input("Masukkan data dalam tuple (pisahkan dengan koma): ").split(","))
set_data = set(tuple_data)

print("Tuple sebelum konversi:", tuple_data)
print("Set setelah konversi:", set_data)

# Set menjadi Tuple
set_data = input("Masukkan data dalam set (pisahkan dengan koma): ").split(",")
tuple_data = tuple(set_data)

print("Set sebelum konversi:", set_data)
print("Tuple setelah konversi:", tuple_data)