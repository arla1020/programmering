
while True:
    print("Skriv in ett nummer")

    number_1 = input()
    done = input()

    try:
        number_1 = int(number_1)
        done = int(done)
    except ValueError:
        print("Nej, det där var inte ett nummer")