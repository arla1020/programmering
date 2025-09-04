print("Hur gammal e du")
age = input ()
age = int(age)

if age <=14:
    print("barnbiljett - 16kr")

elif age <=20:
    print("ungdomsbiljett - 20kr")

elif age <=64:
    print ("ordinarie - 27kr")

elif age <=121:
    print("seniorbiljett - 21kr")

elif age >=122:
    print("fribiljett - 0kr, hur lever du?")