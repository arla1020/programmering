class Vehicle:
    def __init__(self, brand, model, year, color, milage, rent_price, buy_price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.milage = milage
        self.rent_price = rent_price
        self.buy_price = buy_price

    def drive(self, distance):
        self.milage += distance

    def info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        print("Milage:", self.milage)
        print("Rent price:", self.rent_price)
        print("Buy price:", self.buy_price)


class Bil(Vehicle):
    def __init__(self, brand, model, year, color, milage, rent_price, buy_price, ac_on):
        super().__init__(brand, model, year, color, milage, rent_price, buy_price)
        self.ac_on = ac_on

    def toggle_ac(self):
        if self.ac_on == True:
            self.ac_on = False
        else:
            self.ac_on = True


class Motorcyckel(Vehicle):
    def __init__(self, brand, model, year, color, milage, rent_price, buy_price, bike_type):
        super().__init__(brand, model, year, color, milage, rent_price, buy_price)
        self.bike_type = bike_type
        self.riding_mode = "normal"

    def toggle_riding_mode(self):
        if self.riding_mode == "normal":
            self.riding_mode = "eco"

        elif self.riding_mode == "eco":
            self.riding_mode = "sport"

        else:
            self.riding_mode = "normal"


class Lastbil(Vehicle):
    def __init__(self, brand, model, year, color, milage, rent_price, buy_price, load, max_load):
        super().__init__(brand, model, year, color, milage, rent_price, buy_price)
        self.load = load
        self.max_load = max_load

    def add_load(self, weight):
        if self.load + weight <= self.max_load:
            self.load += weight
            print("Load added")
        else:
            print("Too much load")


class Arbetsmotor(Vehicle):
    def __init__(self, brand, model, year, color, milage, rent_price, buy_price):
        super().__init__(brand, model, year, color, milage, rent_price, buy_price)


class FinBil(Vehicle):
    def __init__(self, brand, model, year, color, milage, rent_price, buy_price):
        super().__init__(brand, model, year, color, milage, rent_price, buy_price)


vehicles = []

car1 = Bil("Volvo", "V70n", 2006, "Vit", 55690, 600, 28000, False)
car2 = FinBil("Volkswagen", "Passat B6 Variant", 2008, "Grå", 255800, 900, 40000)
bike1 = Motorcyckel("Yamaha", "R1", 2020, "Blå", 12000, 700, 140000, "sport")
truck1 = Lastbil("Scania", "R500", 2018, "Vit", 400000, 1500, 600000, 0, 20000)
work1 = Arbetsmotor("BRP", "Can-Am Outl.Xxc 1000", 2019, "Flerfärgad", 2486, 5400, 168000)

vehicles.append(car1)
vehicles.append(car2)
vehicles.append(bike1)
vehicles.append(truck1)
vehicles.append(work1)


running = True

while running:

    print()
    print("1. Show vehicles")
    print("2. Add vehicle")
    print("3. Sell vehicle")
    print("4. Rent vehicle")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":

        for vehicle in vehicles:
            print(vehicle.year, vehicle.model, vehicle.color, vehicle.__class__.__name__)

    elif choice == "2":

        print("1. Bil")
        print("2. Motorcyckel")
        print("3. Lastbil")
        print("4. Arbetsmotor")

        vehicle_type = input("Choose vehicle type: ")

        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        color = input("Color: ")
        milage = float(input("Milage: "))
        rent_price = float(input("Rent price: "))
        buy_price = float(input("Buy price: "))

        if vehicle_type == "1":

            ac_on = False

            new_car = Bil(
                brand,
                model,
                year,
                color,
                milage,
                rent_price,
                buy_price,
                ac_on
            )

            vehicles.append(new_car)

        elif vehicle_type == "2":

            bike_type = input("Bike type: ")

            new_bike = Motorcyckel(
                brand,
                model,
                year,
                color,
                milage,
                rent_price,
                buy_price,
                bike_type
            )

            vehicles.append(new_bike)

        elif vehicle_type == "3":

            load = int(input("Load: "))
            max_load = int(input("Max load: "))

            new_truck = Lastbil(
                brand,
                model,
                year,
                color,
                milage,
                rent_price,
                buy_price,
                load,
                max_load
            )

            vehicles.append(new_truck)

        elif vehicle_type == "4":

            new_work = Arbetsmotor(
                brand,
                model,
                year,
                color,
                milage,
                rent_price,
                buy_price,
            )

    elif choice == "3":

        for i in range(len(vehicles)):
            print(i, vehicles[i].model)

        sell_index = int(input("Choose vehicle to sell: "))

        print("Vehicle sold for", vehicles[sell_index].buy_price)

        vehicles.pop(sell_index)

    elif choice == "4":

        for i in range(len(vehicles)):
            print(i, vehicles[i].model)

        rent_index = int(input("Choose vehicle to rent: "))

        days = int(input("How many days: "))

        total_price = days * vehicles[rent_index].rent_price

        print("Total cost:", total_price)

    elif choice == "5":

        running = False