
# priser på produkterna
prices = {
    "Hamburgare": 50,
    "Pommes frites": 25,
    "Läsk": 20,
    "Milkshake": 30,
    "Sallad": 45,
    "McNuggets": 35
}

# Varje item i listan är försäljningen för en hel dag.

sales_data = [
{"Hamburgare": 150, "Pommes frites": 200, "Läsk": 180, "Milkshake": 40, "Sallad": 30, "McNuggets": 100},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 190, "Milkshake": 50, "Sallad": 35, "McNuggets": 105},
{"Hamburgare": 160, "Pommes frites": 210, "Läsk": 185, "Milkshake": 45, "Sallad": 33, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallad": 40, "McNuggets": 115},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 195, "Milkshake": 50, "Sallad": 38, "McNuggets": 120},
{"Hamburgare": 190, "Pommes frites": 240, "Läsk": 210, "Milkshake": 60, "Sallad": 42, "McNuggets": 125},
{"Hamburgare": 185, "Pommes frites": 235, "Läsk": 205, "Milkshake": 58, "Sallad": 40, "McNuggets": 130},
{"Hamburgare": 175, "Pommes frites": 225, "Läsk": 190, "Milkshake": 52, "Sallad": 36, "McNuggets": 120},
{"Hamburgare": 165, "Pommes frites": 215, "Läsk": 185, "Milkshake": 48, "Sallad": 34, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallad": 39, "McNuggets": 115}
]

#beräkna inkomster för varje dag
inkomster_per_dag = []

for day in sales_data:
    total = 0
    for key in day.keys():
        revenue = day[key] * prices[key]
        total += revenue
    
    inkomster_per_dag.append(total)

print(inkomster_per_dag)