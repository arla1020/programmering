while True:
    #maxpoäng / va du fick
    maxpoäng = float(input("Skriv in maxpoängen för provet:"))
    poäng = float(input("Skriv hur mycket poäng du fick:"))

    procent = (poäng / maxpoäng) * 100



    # räkna betygen
    if procent >= 90:
        betyg = "A"

    elif procent >= 80:
        betyg = "B"

    elif procent >= 70:
        betyg = "C"

    elif procent >= 60:
        betyg = "D"

    elif procent >= 50:
        betyg = "E"

    elif procent < 50:
        betyg = "F"

    else:
        betyg = "F"

    # skriv resultatet
    print(f"Du fick {procent:.1f}% och betyget {betyg}.")