# Modifikasi String
a = "Ammar Shiddiq"

# Huruf Besar
print(a.upper()) # Output -> AMMAR SHIDDIQ

# Huruf kecil
print(a.lower()) # Output -> ammar shiddiq

# Menghapus Spasi Putih = adalah spasi pada awal dan akhir string
print(a.strip()) # Output -> "Ammar Shiddiq" bukan " Ammar Shiddiq"

# Memisahkan String
b = "Hello, Ammar"
print(b.split(",")) # Output -> ['Hello', ' Ammar']

# Menggabungkan String = bisa menggunakan operator tambah (+)
c = "Hello"
d = "World"
e = c + ", " + d # tambahkan spasi dan koma
print(e)