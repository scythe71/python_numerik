# Elif adalah pernyataan bersyarat tambahan setelah if
# Elif hanya akan dieksekusi jika kondisi if sebelumnya bernilai False
a = 30
b = 20

if a > b:
    print("a lebih besar dari b") # Tidak TerOutput
elif a == b:
    print("a sama dengan b") # Output: a lebih besar dari b 

# Jika pada bahasa lain dikenal dengan else if
# Maka pada Python dikenal dengan elif