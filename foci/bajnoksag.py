class Adat():
    def __init__(self,sor):
        egy = sor.rstrip("\n").split(";")
        self.csapat = egy[0]
        self.helyezes = int(egy[1])
        self.valtozas = int(egy[2])
        self.pontszam = int(egy[3])
f = open("adatok.txt", encoding = "utf-8")
be = f.readlines()
lista = []
for x in be[1:]:
    egysor = Adat(x)
    lista.append(egysor)
    

#teszt ciklus

for x in lista:
    print(x.csapat, " ", x.pontszam)

"""
sorok_szama = len(lista)
print(f"3.feladat: A bajnokságon résztvevő csapatok száma {sorok_szama}")

pontok = []

for x in lista:
    
    pontok.append(x.pontszam)

#print(pontok)

osszpont = sum(pontok)
#print(osszpont)

atlag = osszpont / sorok_szama


print("4.feladat: A csapatok átlagos pontszáma: {:.2f} pont".format(atlag))
    

"""
"""
szamlalo = 0
for x in lista:
    szamlalo +=1
print("3. feladat: A bajnokságon résztvevő csapatok száma:", szamlalo)
osszeg = 0
for x in lista:
    osszeg = osszeg + x.pontszam
atlag = osszeg / szamlalo
print("4. feladat: A csapatok átlagos pontszáma:", atlag, "pont")
szamlalo = 0
y = -100
for x in lista:
    if x.valtozas > y:
        y = x.valtozas
for x in lista:
    if x.valtozas == y:
        print("5. feladat: A legtöbbet javító csapat:", x.csapat)
a = False

for x in lista:
    if x.csapat == "Németország":
        a = True
if a == True:
    print("6. feladat: A csapatok között Németország is ott van")
if a == False:
    print("6. feladat: A csapatok között nincs ott Németország")
   """     
    

        
