#---0===5---8===11---
angka = float(input("Masukkan rentang angka dari 0 sampai 5\n---0===5--- : "))
nol = (angka > 0) 
lima = (angka < 5)
hasil1 = nol and lima
#print("0 sampai 5 = ", hasil1)

angka = float(input("Masukkan rentang angka dari 8 sampai 11\n---8===11--- : "))
lapan = (angka > 8) 
sebelas = (angka < 11)
hasil2 = lapan and sebelas
#print("8 sampai 11 = ", hasil2)

hasilnya = hasil1 and hasil2
print("---0===5---8===11--- = ", hasilnya)

#===0---5===8---11===
angka = float(input("Masukkan angka dibawah 0 atau rentang angka 5 sampai 8\n===0---5=== : "))
nol = (angka < 0) 
lima = (angka > 5)
hasil1 = nol or lima
#print("0 sampai 5 = ", hasil1)

angka = float(input("Masukkan rentang angka dari 5 sampai 8 atau lebih dari 11\n===8---11=== : "))
lapan = (angka < 8) 
sebelas = (angka > 11)
hasil2 = lapan or sebelas
#print("8 sampai 11 = ", hasil2)

hasilnya = hasil1 and hasil2
print("===0---5===8---11=== = ", hasilnya)
