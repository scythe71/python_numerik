# Variabel yang dibuat di luar fungsi disebut variabel global
x = "awesome"

def myfunc():
  print("Python is " + x) # Akan mencetak var global = awesome
myfunc()

# Variabel yang dibuat di dalam fungsi adalah variabel lokal 
# dan hanya dapat digunakan di dalam fungsi tersebut
# Var x global tidak dapat diakses di dalam fungsi jika ada var lokal dengan nama yang sama
def myfunc2():
  x = "fantastic"
  print("Python is " + x) # Akan mencetak var lokal = fantastic
myfunc2()

print("Python is " + x) # Akan tetap sama = awesome