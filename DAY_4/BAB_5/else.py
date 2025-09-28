# Else adalah sebuah blok opsional yang dapat ditambahkan setelah if atau elif.
# Blok else akan dieksekusi jika semua kondisi pada if dan elif bernilai False

nilai = 75
if nilai >= 85:
    print("Selamat! Anda mendapatkan nilai A.")
elif nilai >= 70:
    print("Anda mendapatkan nilai B.") # Juga bisa tanpa menggunakan elif
else:
    print("Anda harus belajar lebih giat lagi.")