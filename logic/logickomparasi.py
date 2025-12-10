#gabungan area rentang dari angka
#===3------5===
inputUser = float(input('Masukkan angka yang bernilai \nkurang dari 3 atau lebih dari 5\n ===3xxxx5===:'))

#===3------
isKurangDari = (inputUser < 3)
#print("Kurang dari 3 =",isKurangDari)

#------5===
isLebihDari = (inputUser > 5)
#print("Lebih dari 5 =",isLebihDari)

#===3------5===
isCorrect = isKurangDari or isLebihDari
print("Jawaban = ",isCorrect)

#---3======5---
inputUser = float(input('\n\nMasukkan angka yang bernilai \nlebih dari 3 dan kurang dari 5\n xxx3======5xxx:'))

#===3------
isLebihDari = (inputUser > 3)
#print("Kurang dari 3 =",isKurangDari)

#------5===
isKurangDari = (inputUser < 5)
#print("Lebih dari 5 =",isLebihDari)

#---3======5---
isCorrect = isLebihDari and isKurangDari
print("Jawaban = ",isCorrect)