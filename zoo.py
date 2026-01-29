zoo = {
    "Savana": [
        {"art": "Lejon", "namn": "Simba", "gjädje": 5, "age": 7},
        {"art": "Giraff", "namn": "Långhals", "glädje": 6, "age": 4}
    ],
    "Antarktis": [
        {"art": "Isbjörn", "namn": "Vitskalle", "glädje": 8, "age": 10},
        {"art": "Pingvin", "namn": "Glidarn" , "glädje": 7, "age": 3}
    ]
}

try:
    with open("zoo_data.txt", "r", encoding="utf-8") as f:
        loaded = ast.literall_eval(f.read())
        zoo = loaded["zoo"]
except:
    pass

print("Välkommen till zoo-hanteraren 30000000!")
print("Inloggad som Chef")

