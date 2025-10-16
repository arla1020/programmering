
BASE_PRICE = 70

pizza = []

# Fyll på med flera ingredienser
ingredients = [
    ("Tomatsås", 20),       #pos 0
    ("Ost", 25),            #pos 1
    ("Skinka", 15),         #pos 2
    ("Pepperoni", 20),      #pos 3
    ("Annanas😭💀", 1),    #pos 4
]

ingredientsNoKr = [
    ("Tomatsås"),           #pos 0             #
    ("Ost"),                #pos 1             #
    ("Skinka"),             #pos 2             # den här delen används inte
    ("Pepperoni"),          #pos 3             #
    ("Annanas😭💀")        #pos 4             #
]


print("Välkommen till pizzabagaren 3000")
while True:
    print("Vad vill du göra?")
    print("1. Visa Möjliga Ingredienser")
    print("2. Lägga till en ingrediens")
    print("3. Ta bort en ingrediens")
    print("4. Visa Pizza")
    print("5. Räkna ut pris")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        print("Våra ingridienser")
        for ingredient in ingredients:
            print(f"{ingredient[0]} : {ingredient[1]}kr")

    elif choice == "2":
        print("vilken ingridiens vill du he på pizzan")
        for ingredient in ingredients:
            print(f"{ingredient[0]}")
        namn = input()
        pizza.append(namn)        

    elif choice == "3":
        print("Vilken ingridiens vill du ta bort?")
        print("Du har just nu", pizza, "på din pizza")
        namn = input()
        if namn in pizza:
            pizza.remove(namn)

    elif choice == "4":
        
        print("Din pizza har", pizza)

    elif choice == "5":
        total = 0
        for ingredient in pizza:
            for ingredient2 in ingredients:
                if ingredient == ingredient2[0]:
                    total += ingredient2[1]
        
        total += BASE_PRICE
        print("Totala priset för din pizza:", total)

    elif choice == "q":
        print("Stänger ner...")
        break

    else:
        print("Ogiltigt Svar")
    

    input("\nTryck enter för att fortsätta...")