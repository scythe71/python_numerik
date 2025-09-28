# Else pada perulangan for adalah pernyataan yang akan dieksekusi ketika perulangan for telah selesai.

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Note: Else tidak akan dieksekusi jika perulangan for dihentikan dengan break
for x in range(6,10):
    print(x)
    if x == 8: break
else:
    print("Finally finished!") # pernyataan ini tidak akan pernah tereksekusi