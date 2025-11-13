
swedish_to_english = {
    "apelsin" : "orange",
    "bil" : "car",
    "vattenmelon" : "watermelon"
}

# Key : Value

print(swedish_to_english["bil"])

# ändra nånting
swedish_to_english["vattenmelon"] = "melonvater"

# ta bort nånting
swedish_to_english.pop("vattenmelon")

volvo = {
    "model" : "740",
    "electric" : False,
    "color" : ["gul", "brun"]
}

print(f"Volvo {volvo{'model'}}. Är den elektrisk {volvo['electric']}")