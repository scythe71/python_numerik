# Ada tiga tipe numerik di Python: int, float, dan complex.

x = 5           # int
y = 3.14        # float
z = 1j          # complex

# Untuk Memeriksa tipe data, gunakan fungsi type()
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

# Integer (int)
a = 1
b = 35656222554887711
c = -3255522
print(type(a), type(b) + type(c))  # Output: <class 'int'>

# Float
d = 1.10
e = 1.0
f = -35.59

# Float juga bisa ditulis dalam notasi ilmiah dengan "E" atau "e"
g = 35e3 # 35 x 10^3
h = 12E4  # 12 x 10^4
i = -87.7e100 # -87.7 x 10^100
print(type(d), type(e), type(f), type(g), type(h), type(i)) # Output: <class 'float'>

# Complex
# Complex ditulis dengan "j" sebagai bagian imajiner
j = 3+5j
k = 5j
l = -5j
print(type(j), type(k), type(l)) # Output: <class 'complex'>

# Convert type data
m = float(a)        # Convert int ke float
n = int(d)          # Convert float ke int
o = complex(a)      # Convert int ke complex
print(m, n, o)      # Output: 1.0, 1, (1+0j)
print(type(m), type(n), type(o))  # Output: <class 'float'>, <class 'int'>, <class 'complex'>

# Note: Complex tidak bisa di convert ke int atau float