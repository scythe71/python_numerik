# Fungsi bisa mengembalikan nilai boolean
def myfunc():
    return True
print(myfunc()) # Output: True

if myfunc():
    print("YES") # Output: YES
else:
    print("NO") # Tidak TerOutput

# python juga memiliki fungsi bawaan isInstance()
# yautu fungsi yang mengecek apakah objek memiliki tipe tertentu 
# dan mengembalikan nilai boolean
x = 200
print(isinstance(x, int)) # Output: True
print(isinstance(x, str)) # Output: False