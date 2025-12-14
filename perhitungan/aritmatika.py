a = 20
b = 40
c = 2
d = 5

hasil = a + b
print(a, "+", b, "=", hasil)

hasil = a - b
print(a, "-", b, "=", hasil)

hasil = a * b
print(a, "x", b, "=", hasil)

hasil = a / b
print(a, "/", b, "=", hasil)

#eksponen (pangkat)
hasil = c ** d
print(c, "^", d, "=", hasil)

#modulus
hasil = d % c
print(d, "%", c, "=", hasil)

#floor division
hasil = d // c
print(d, "//", c, "=", hasil)

#prioritas
'''
    1. ()
    2. eksponen ** (pangkat)
    3. perkalian, pembagian, floor division, modulus
    4. penjumlahan, pengurangan
'''
o = 4 
j = 3
s = 2
hasil =  o ** s * o + s / j - j % o // s
print(o ,'**',s ,'*' ,o ,'+' ,s ,'/', j ,'-', j ,'%', o, '//', s, "hasil=", hasil)