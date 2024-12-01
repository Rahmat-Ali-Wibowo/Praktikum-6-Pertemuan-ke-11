import math

# Fungsi a menggunakan lambda
a = lambda x: x**2

# Fungsi b menggunakan lambda
b = lambda x, y: math.sqrt(x**2 + y**2)

# Fungsi c menggunakan lambda
c = lambda *args: sum(args) / len(args)

# Fungsi d menggunakan lambda
d = lambda s: "".join(set(s))

# Contoh penggunaan fungsi-fungsi lambda
print(a(5))          # Output: 25
print(b(3, 4))       # Output: 5.0
print(c(1, 2, 3, 4)) # Output: 2.5
print(d("hello"))    # Output: helo (atau variasi lain karena set tidak berurutan)
