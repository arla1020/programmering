
while True:
    print("Skriv in ett nummer")

    number_1 = input()
    number_2 = input()

    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        print("Det där var inte ett nummer")
