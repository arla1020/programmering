shop = {
    
    "turbo KP35-005" : { "price" : 6869, "amount" : 4 },
    "avgasrör" : {"price" : 274.5, "amount" : 12},
    "MOBIL 2-taktsolja 2-T 1L" : {"price" : 195, "amount" : 52},
    "AUDI R8 v10 performance" : {"price" : 1971500, "amount" : 1},
    "dildo dekoration sugpropp" : {"price" : 367, "amount" : 6}

}

sales = []
# lägg spar text dokument grejerna här, innan while true loopen
import ast

#ladda tidigare data
try:
    with open("butik_data.txt", "r", encoding="utf-8") as f:
        data = ast.literal_eval(f.read())
        shop = data["shop"]
        sales = data["sales"]
except:
    pass


print("Välkommen till Butikshanteraren 3000")
print('Inloggad som Butiksägare')
while True:
    print("Vad vill du göra?")
    print("1. Visa alla varor")
    print("2. Lägg till en ny vara")
    print("3. Ändra priset på vara")
    print("4. Fylla på vara")
    print("5. Sälja en vara")
    print("6. Visa total intäkter")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        for product in shop:
            print (f"{product} {shop[product]}")

    
    elif choice == "2":   # fråga användaren vilken vara, priset på vara
        print("Vad vill du lägga till?")
        name = input()
        print("Vad ska den kosta?")
        price = input()
        print("Hur många har du köpt in?")
        amount = input()

        price = int(price)
        amount = int(amount)

        shop.update({name : {"price" : price, "amount" : amount}})

        print("La till produkten!")
        

    elif choice == "3":
        print("Vilken vara vill du ändra priset på?")
        name = input()
        print("Vad ska du ändra priset till?")
        price = input()

        price = int(price)

        shop[name]["price"] = price

        print("Ändrade priset!!")

    elif choice == "4":
        print("Vilken vara vill du fylla på?")
        name = input()
        print("Hur många vill du lägga till?")
        amount = input()
        
        amount =int(amount)

        shop[name]["amount"] += amount        
        print("Fyllde på produkten!")


    elif choice == "5":    # sälja en vara
        print("Vilken vara ska du sälja")
        name = input()
        print("Hur många ska du sälja")
        amount = input()

        amount = int(amount)

        shop[name]["amount"] -= amount

        sales.append({name : {"amount" : amount, "price" : shop[name]["price"]}})

    elif choice == "6":     # visa alla intäkter   ta price * amount

        total = 0
        for sale in sales:
            for item in sale:
                amount = sale[item]["amount"]
                price = sale[item]["price"]
                total += amount * price

        
        print (f"Totala intäkter = {total} kr")

    elif choice == "q":
        #spara till fil
        with open("butik_data.txt", "w", encoding="utf-8") as f:
            f.write(str({"shop": shop, "sales": sales}))
        break
    else:
        print("Ogiltigt Svar")
    
    input("\nTryck enter för att fortsätta...") 