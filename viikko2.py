#Tehtävä 1
print("Tästä alkaa ohjelmointi!")

#Tehtävä 2
print(123456789*987654321)

#Tehtävä 3
kolmeLeveys = 5
kolmeKorkeus = 5

for rivi in range(kolmeKorkeus):
    if rivi == 0 or rivi == kolmeKorkeus - 1:
        print("#" * kolmeLeveys)
    else:
        print("#" + " " * (kolmeLeveys - 2) + "#")

#Tehtävä 4
neljaLeveys = 7

for i in range(1, neljaLeveys + 1, 2):
    print(" " * ((neljaLeveys - i) // 2) + "*" * i)

print(" " * (neljaLeveys // 2) + "*")

#Tehtävä 5
viisiE = 3
viisiB = 1
viisiC = viisiE + viisiB
viisiVastaus = str(viisiC)
print("Tehtävä 5 = " + viisiVastaus)
#Tulokset olivat samat kun laskin käsin.

#Tehtävä 6
kuusiB = 4
kuusiB = kuusiB + 1
kuusiB = kuusiB + 1
kuusiB = kuusiB + 1
kuusiVastaus = str(kuusiB)
print("Tehtävä 6 = " + kuusiVastaus)
#Samanlainen tulos kun laskin päässä

#Tehtävä 7
sevenC = 1
sevenB = 3
sevenC = sevenC+sevenB
sevenB = sevenC+sevenB
sevenC = sevenC+sevenB
sevenVastaus = str(sevenC)
print("Tehtävä 7 = " + sevenVastaus)
#Vähän vaikeammin laskea käsin, mutta tulokset olivat samat.

#Tehtävä 8
kahdeksanA = 4
kahdeksanC = 3
kahdeksanB = kahdeksanA + 2 * kahdeksanC
kahdeksanD = kahdeksanA + kahdeksanC + kahdeksanB
kahdeksanVastaus = str(kahdeksanD)
print("Tehtävä 8 = " + kahdeksanVastaus)
#Samanlainen tulos kun laskin päässä

#Tehtävä 9
nineC = 5
nineA = 4
nineD = nineC
nineC = nineA
nineA = nineD
nineVastaus = str (nineA)
print("Tehtävä 9 = " + nineVastaus)
#Samanlainen tulos kun laskin päässä

#Tehtävä 10
tenC = 2
tenC = tenC * tenC
tenC = tenC * tenC
tenC = tenC * tenC
tenC = tenC * tenC
tenVastaus = str(tenC)
print("Tehtävä 10 = " + tenVastaus)
#Ei oikeen voinu laskea päässä 2^16