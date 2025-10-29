# Else pada perulangan for adalah pernyataan yang akan dieksekusi ketika perulangan for telah selesai.
for x in range(6):
    print(x) # Output: 0, 1, 2, 3, 4, 5
else:
    print("Finally finished!") # Output: Finally finished!

# Note: Else tidak akan dieksekusi jika perulangan for dihentikan dengan break
for x in range(6,10):
    print(x) # Output: 6, 7, 8
    if x == 8: break
else:
    print("Finally finished!") # pernyataan ini tidak akan pernah tereksekusi