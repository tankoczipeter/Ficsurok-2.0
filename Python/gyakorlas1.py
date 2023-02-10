#1
"""
j = []
for x in range(1,4,1):
    l = int(input("Kérem adjon meg három számot:"))
j.append(l)
print("A megadott számok közzül a legkisebb érték",min.(j))
"""
#2
"""
p = int(input("Kérem adja meg a számot"))
p1 = int(input("Kérem adja meg a számot"))
p2 = int(input("Kérem adja meg a számot"))

if p != p1 and p1 != p2 and p2 != p:
    print("A megadott számok különböznek")
"""
#3
"""
d = int(input("Kérem a pontszámokat:"))

if d <= 50:
    print("Az érdemjegy 1-es")
if 50 < d <= 60:
    print("Az érdemjegy 2-es")
if 60 < d <= 70:
    print("Az érdemjegy 3-es")
if 70 < d <= 80:
    print("Az érdemjegy 4-es")
if d >= 80:
    print("Az érdemjegy 5-es")
"""
#4
"""
van = False
h = int(input("Kérem adja meg a pontszámokat:"))
if h % 3 == 0 or h % 5 == 0:
    van = True
if van:
    print("A megadott szám osztható 3-val és 5-vel")
else:
    print("A megadott szám nem osztható")
"""
#5
"""   
p1 = int(input("Kérem adja meg a számot:"))
p2 = int(input("Kérem adja meg a számot:"))
p3 = int(input("Kérem adja meg a számot:"))
if p1 + p2 == p3 or p2 + p3 == p1 or p1 + p3 == p2:
    print("A megadott számok közül valamelyik 2 szám összege a 3. ")
else:
    print("A megadott szamok közül egyik sem összege a 3.")
"""
#6
"""
paros = False
for x in range(1,4,1):
    p = int(input("Kérem adja meg a számot:"))
    if p % 2 == 0:
        paros = True
if paros:
    print("Van benne páros szám:")
else:
    print("Nincs benne páros szám")
"""
#8
"""
a = int(input("Kérem a számot:"))
b = float(input("Kérem a számot:"))

c = a**b
print("A két szám hatványa",c)
"""
#9
"""
p = int(input("Kérem adja meg 20-nál kisebb számot:"))
r = ""
print(r*p,"START")
"""
#27
"""
i = [1,2,3,4,5]
i.sort()
i.reverse()
print(i)
"""
#26
"""
i = [1,2,3,4,5]
k = []
k.append(i)
print(k)
"""






