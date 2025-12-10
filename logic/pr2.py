#---0===5---8===11---
angka = float(input("Masukkan angka\n---0===5---\n:"))
nol = (angka > 0) 
lima = (angka < 5)
hasil1 = nol and lima
#print("0 sampai 5 = ", hasil1)

angka = float(input("Masukkan angka\n---8===11---\n:"))
lapan = (angka > 8) 
sebelas = (angka < 11)
hasil2 = lapan and sebelas
#print("8 sampai 11 = ", hasil2)

hasilnya = hasil1 and hasil2
print("---0===5---8===11---", hasilnya)

#===0---5===8---11===
angka = float(input("Masukkan angka\n===0---5===\n:"))
nol = (angka < 0) 
lima = (angka > 5)
hasil1 = nol or lima
#print("0 sampai 5 = ", hasil1)

angka = float(input("Masukkan angka\n===8---11===\n:"))
lapan = (angka < 8) 
sebelas = (angka > 11)
hasil2 = lapan or sebelas
#print("8 sampai 11 = ", hasil2)

hasilnya = hasil1 and hasil2
print("===0---5===8---11===", hasilnya)
