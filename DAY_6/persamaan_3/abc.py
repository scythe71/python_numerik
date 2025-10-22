import math

def akarD(a, b, c):
    D = b**2 - 4*a*c # Diskriminan
    aD = math.sqrt(D)

    if D < 0:
        return "Tidak punya akar real"
    
    x1 = (-b + aD) / (2*a)
    x2 = (-b - aD) / (2*a)
    return [x1, x2]

x = akarD(2, 3, -4)

def ctk():
    for i, xnum in enumerate(x):
        print(f"x{i+1} =  {xnum:.5f}")