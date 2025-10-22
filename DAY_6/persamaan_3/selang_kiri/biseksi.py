from .. import abc

def f(x):
    return 2*x**2 + 3*x - 4 # Fungsi f(x)

# input awal interval
a = -4
b = 0
c = (a + b) / 2
toleransi = 0.00001
iterasi = 1
x2 = abc.x[1]

c_pref = 0
Era = 100

fa = f(a)
fb = f(b)
fc = f(c)

# Pastikan ada akar di antara a dan b
if f(a) * f(b) > 0:
    print("Tidak ada akar di antara interval [a,b]")

else:
    print("="*45 + "BISEKSI" + "="*45)
    print(f"{'Iterasi':<8}{'a':<10}{'b':<10}{'c':<13}{'f(a)':<10}{'f(b)':<10}{'f(c)':<10}{'Interval baru':<18}{'Era'}")
    print("-"*98)
    print(f"{iterasi:<8}{a:<10.3f}{b:<10.3f}{c:<13.5f}{fa:<10.3f}{fb:<10.3f}{fc:.5f}")

    while Era > toleransi:
        c = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fc = f(c)

        tanda = f(a) * f(c)
        if tanda < 0:
            interval = f"[{a:.3f}, {c:.3f}]"
            # interval = "[a, c]"
            b = c
        else:
            interval = f"[{c:.3f}, {b:.3f}]"
            # interval = "[c, b]"
            a = c
        
        if c != 0:
            Era = abs((c - c_pref) / c)
        c_pref = c

        print(f"{iterasi:<8}{a:<10.3f}{b:<10.3f}{c:<13.5f}{fa:<10.3f}{fb:<10.3f}{fc:<10.3f}{interval:<18}{Era:.6f}")
        iterasi += 1
    
    print("-"*98)
    akar = (a + b) / 2
    print(f"\nAkar hampiran = {akar:.4f}")
    print(f"Nilai Asli = {x2:.4f}")