# fungsi range() berfungsi untuk membuat daftar angka
for x in range(6): # range(6) bukan dari 0-6 tetapi 0-5
    print(x) # Output: 0, 1, 2, 3, 4, 5

# fungsi range() default index awal adlah 0, tetapi bisa juga diatur seperti:
for x in range(13-5, 10):
    print(x) # Output: 8, 9

# fungsi range() default menambah (+ 1) di setiap iterasi, tetapi bisa juga diatur seperti:
for x in range(13, 20, 5):
    print(x) # Output: 13, 18