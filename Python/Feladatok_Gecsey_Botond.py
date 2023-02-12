#1
"""
j = []
for x in range (1,4,1):
    l = int(input("Kérem adjon meg egy számot:"))
    j.append(l)
print("A megadott számok közül a legkisebb:",min(j))

#2
p1 = int(input("Kérem adjon meg egy számot:"))
p2 = int(input("Kérem adjon meg egy számot:"))
p3 = int(input("Kérem adjon meg egy számot:"))
if p1 != p2 and p2 != p3 and p3 != p1:
    print("A megadott számok mind különbözőek")
else:
    print("A megadott számok nem egyeznek meg")

#3
h = int(input("Kérem adja meg dolgozata pontszámát:"))
if h <= 50:
    print("A kapott érdemjegye 1-es")
if 50< h <= 60:
    print("A kapott érdemjegye 2-es")
if 60< h <= 70:
    print("A kapott érdemjegye 3-as")
if 70< h < 85:
    print("A kapott érdemjegye 4-es")
if h >= 85:
    print("A kapott érdemjegye 5-ös")
#4
van = False
g = int(input("Kérem adja meg dolgozata pontszámát:"))
if g % 3 == 0 or g % 5 == 0:
    van = True
if van:
    print("A megadott szám osztható 3-al vagy 5-el.")
else:
    print("A megadott szám nem osztható 3-al vagy 5-el")

#5
p4 = int(input("Kérem adjon meg egy számot:"))
p5 = int(input("Kérem adjon meg egy számot:"))
p6 = int(input("Kérem adjon meg egy számot:"))
if p4 + p5 == p6 or p4 + p6 == p5 or p6 + p5 == p4:
    print("A bekért számok közül valamely 2 szám összege a 3.")
else:
    print("A bekért számok közül egyik 2 szám összege sem a 3.")

#6

p7 = int(input("Kérem adjon meg egy számot:"))
p8 = int(input("Kérem adjon meg egy számot:"))
p9 = int(input("Kérem adjon meg egy számot:"))
if p7 % 2 == 0 and p8 % 2 == 0 and p9 % 2 == 0:
    print("Mind a 3 szám osztható 2-vel")
else:
    print("Nem mind a 3 szám osztható 2-vel")
    
#8

a = int(input("Adjon meg egy számot:"))
b = float(input("adjonmeg egy számot:"))
c = a**b
print("A két szám hatványa:",c)

#27
i = [1,2,3,4,5]
i.sort()
i.reverse()
print(i)

#26
i = [1,2,3,4,5]
k = i.copy()
print(k)

#9
d = int(input("Adjon meg egy 20-nál kisebb pozitív számot:"))
r = " "
print(r*d,"START")
#7
szam6=int(input("Kérem adjon meg egy pozitív egész számot:"))

if szam6 <= 3:
    print("Nics tőle kisebb 3-mal osztható pozitív egész szám.")

else:
    x = 3
    while szam13 > x:
        if x %3 == 0:
            print(x)
        x += 1
"""
#23
szov = input("Kérem adjon meg egy mondatot: ")
list = szov.split(" ")
list.reverse()
for x in list:
    print(x, end=" ")