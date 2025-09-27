# Fungsi bisa mengembalikan nilai boolean
def myfunc():
    return True
print(myfunc()) # Output: True

if myfunc():
    print("YES")
else:
    print("NO") # Output: YES

# python juga memiliki fungsi bawaan isInstance()
x = 200
print(isinstance(x, int)) # Output: True
print(isinstance(x, str)) # Output: False