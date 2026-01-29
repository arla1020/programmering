from nicegui import ui
import random

text = ui.label("Välj nå fö faen")

def spela(val):
    val_lista=["Sten","Sax","Påse"]
    dator = random.choice(val_lista)
    if val==dator:
        resultat.text=f"Oavgjort! Båda valde {val}."
    elif(val=="Sten" and dator == "Sax") or \
        (val=="Sax" and dator == "Påse") or \
        (val=="Påse" and dator == "Sten"):
        resultat.text=f"Du vann!{val} slår {dator}."
    else:
        resultat.text=f"Datorn vann! {dator} slår {val}."

ui.button("Sten", on_click=lambda: spela("Sten"))
ui.button("Sax", on_click=lambda: spela("Sax"))
ui.button("Påse", on_click=lambda: spela("Påse"))

resultat=ui.label("Lycka till tjockis")

ui.run(native= True)