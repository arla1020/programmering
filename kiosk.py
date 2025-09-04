glass = 20
varmkorv = 15
läsk = 15
godis = 10

print ("Välkommen till Storsjökiosk!")
print ("Glass - 20kr, Varmkorv - 15kr, Läsk - 15kr, Godis - 10kr")
print ("Vad önskas?")

produkt = input ()
antal =int (input ("Hur många vill du ha"))

pris = 0

if produkt == "glass":
    pris = 20

elif produkt == "varmkorv":
    pris = 15

elif produkt == "läsk":
    pris = 15

elif produkt == "godis":
    pris = 10

elif produkt == "allt":
    pris = 60

total = pris * antal

if pris > 0:
    print("Det kommer att kosta", total, "kr")
else:
    print ("Produkten finns inte här din smartskalle")