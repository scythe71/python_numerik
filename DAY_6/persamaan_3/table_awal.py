def f(x):
    return 2*x**2 + 3*x - 4

# Contoh Penggunaan:
print("=====================")
print("x\t| \tf(x)")
print("---------------------")
for x in range(-3, 4):
    print(f"{x} \t| \t{f(x)}")
print("=====================")