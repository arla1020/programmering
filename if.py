print ("Hej! Hur gammal är du?")
age = input()
age = int(age)

if age < 18:
    print("Du är ett barn")

elif age == 20:
    print("Du är 20")

elif age >= 18 and age <60:
    print("Du är vuxen")

elif age >= 60:
    print("Du e en gamling")

else:
    print("Jag har ingen aning om vad du e")