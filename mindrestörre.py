while True:
    print("skirv in ett nummer")
    number_1 = input()
    try:
        number_1 = int(number_1)
        break
    except:
        print("de där är inte ett numer din pappskalle")

while True:
    print("skriv in ett till nummer (eller 'done' för att avsluta)")
    number_2 = input()

    if number_2 == "done":
        break

    try:
        number_2 = int(number_2)
    except ValueError:
        print("Det där var inte ett nummer")
        continue

    if number_2 > number_1:
        print(number_2, "större än", number_1)
    elif number_2 < number_1:
        print(number_2, "mindre än", number_1)
    else:
        print("nummerna är lika stora")

    number_1 = number_2
