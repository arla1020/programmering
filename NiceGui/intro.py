from nicegui import ui 

def calculate_farennheit(celsius):
    if type(celsius) is not float:
        return
    celsius = float(celsius)
    farenheit = (celsius * 1.8) + 32
    farenheit = round(farenheit, 1)
    result_label.text = f"Det blir: {farenheit}°F"


@ui.page("/fahrenheit")
def fahrenheit_page():
    ui.label("Tjoooo! Välkommen damp unge, skriv in temperaturen i celsius")
    ui.number("Celsuis",
            on_change= lambda e: calculate_farennheit(e.value))

result_label = ui.label("Skirv in temperaturen")

@ui.page("/")
def home_page():
    ui.label("Välj vart du vill")
    ui.link("Celsius till Fahrenheit", fahrenheit_page)
    ui.link("Login sida", "/login/Hasse")

@ui.page("login/{name}")
def login_page(name):
    ui.label(f"Hej {name}!")


ui.run(native=True)