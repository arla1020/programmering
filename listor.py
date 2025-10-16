# skit på marken
marken = ["yxa", "hamburgare", "kebab", "ljussabel"]

# saker i ryggsäcken
backpack = []

while True:
    print("\nvad vill du göra?")
    print("1. Visa Ryggsäckens innehåll")
    print("2. Ta upp nå från marken o he ner i ryggsäcken")
    print("3. He tillbaka saker till marken")
    print("4. Ändra plaserna i ryggsäcken")
    print("q. stäng ner")
    choice = input("Välj: ").strip().lower()

    if choice == "1":
        if backpack:
            print("Ryggsäcken innehåller:", backpack)
        else:
            print("Det finns inget i ryggsäcken")

    elif choice == "2":
        if not marken:
            print("Det finns inge o plocka upp från marken")
            continue
        print("På marken finns de:", marken)
        item = input("Skriv vad du vill plocka upp: ").strip()
        if item in marken:
            marken.remove(item)
            backpack.append(item)
            print(f"{item} las ner i ryggsäcken")
        else:
            print("Föremålet finns inte på marken.")

    elif choice == "3":
        if not backpack:
            print("Finns inge i ryggsäcken — inget att lägga ner på marken.")
            continue
        print("Ryggsäcken innehåller:", backpack)
        item = input("Skriv vad du vill lägga tillbaka på marken: ").strip()
        if item in backpack:
            backpack.remove(item)
            marken.append(item)
            print(f"{item} las tillbaka på marken.")
        else:
            print("Det finns inte det föremålet i ryggsäcken.")

    elif choice == "4":
        if len(backpack) < 2:
            print("Det behöver vara minst två grejer i ryggan för o byta plats.")
            continue
        print("Ordning i ryggsäcken just nu:", backpack)
        try:
            i = int(input("Index på första objekt (0 = första): ").strip())
            j = int(input("Index på andra objekt (0 = första): ").strip())

            if i < 0 or j < 0 or i >= len(backpack) or j >= len(backpack):
                print("Index utanför intervall.")
                continue
            
            backpack[i], backpack[j] = backpack[j], backpack[i]
            print("Bytte plats. Ny ordning:", backpack)
        except ValueError:
            print("Skriv ett giltigt heltal för index.")

    elif choice == "q":
        print("Stänger ner. Tjena Tjena!")
        break

    else:
        print("Ogiltigt val — försök igen.")
