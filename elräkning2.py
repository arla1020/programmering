import datetime

print("Start år")
start_year = int(input())

print("Start månad")
start_month = int(input())

print("Start dag")
start_day = int(input())

print("Slut år")
end_year = int(input())

print("Slut månad")
end_month = int(input())

print("Slut dag")
end_day = int(input())

try:
    start_date = datetime.datetime(start_year, start_month, start_day)
    end_date = datetime.datetime(end_year, end_month, end_day)

    date_diff = (end_date - start_date).days
    print(f"Antal dagar mellan start- och slutdatum: {date_diff}")

    meter_start = int(input("Elmätarens startvärde: "))
    meter_end = int(input("Elmätarns slutvärde: "))
    consumed = meter_end - meter_start

    day_fee = int(input("Dags avgift: "))
    kwh_price = float(input("Pris per kWh: "))

    total_price = (date_diff * day_fee + consumed * kwh_price) * 1.25  # för moms

    print(f"Det totala för din elräkning blir: {total_price:.2f} kr")
except ValueError as e:
    print(f"Ett fel inträffade: {e}")
except Exception as e:
    print(f"Ett oväntat fel inträffade: {e}")