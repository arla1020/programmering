from nicegui import ui 

def calculate_farennheit(celsius):
    if type(celsius) is not float:
        return
    celsius = float(celsius)
    farenheit = (celsius * 1.8) + 32
    farenheit = round(farenheit, 1)
    result_label.text = f"Det blir: {farenheit}°F"

ui.label("Tjoooo! Välkommen damp unge, skriv in temperaturen i celsius")
ui.number("Celsuis",
         on_change= lambda e: calculate_farennheit(e.value))

result_label = ui.label("Skirv in temperaturen")


ui.run(native=True)