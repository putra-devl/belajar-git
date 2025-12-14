#setiap hasil dari komparasi adalah boolean
#>,<,>=,<=,==,!=,is,is not

a = 4
b = 2 

# >
hasil = a > 3
print(a,">",3,"=",hasil)

#<
hasil = a < 5
print(a,"<",5,"=",hasil)

#==
hasil = b == 2
print(b,"==",2,"=",hasil)

#>=
hasil = b >= 5
print(b,">=",5,"=",hasil)

#<=
hasil = b <= 5
print(b,"<=",5,"=",hasil)

#!=
hasil = a != 4
print(a,"!=",4,"=",hasil)

#is
hasil = a is b
print(a,"is",b,"=",hasil)

#is not
hasil = a is not b
print(a,"is not",b,"=",hasil)

print("====")
print("id a =",hex(id(a)))
print("id b =",hex(id(b)))