# Argumen yang berubah-ubah
# Jika Jumlah argumen tidak diketahui, Anda dapat menggunakan argumen *args
def hello(*nama): # dengan menambahkan * di depan argumen maka argumen tersebut menjadi tuple
    print(f"Hello {nama}")

hello("Ammar", "Shiddiq") # Output: Hello ('Ammar', 'Shiddiq')