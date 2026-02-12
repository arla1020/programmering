from nicegui import ui

points = 0

@ui.page('/')
def start_page():
    global points
    points = 0
    ui.label("Quizzer 300+").classes
    ui.button("Starta Quiz", on_click=lambda: ui.navigate.to('/fråga1'))


@ui.page('/fråga1')
def fråga1():

    ui.label("Fråga 1/4")

    ui.label("Vad är 2 + 2?")

    ui.button("3", on_click=lambda: ui.navigate.to('/fråga2'))

    def rätt_svar():
        global points
        points += 1
        ui.navigate.to('/fråga2')

    ui.button("4", on_click=rätt_svar)
    
    ui.button("6", on_click=lambda: ui.navigate.to('/fråga2'))


@ui.page('/fråga2')
def fråga2():

    ui.label("Fråga 2/4")

    ui.label("Vilket språk använder NiceGUI?")

    ui.button("Java", on_click=lambda: ui.navigate.to('/fråga3'))

    def rätt_svar():
        global points
        points += 1
        ui.navigate.to('/fråga3')

    ui.button("Python", on_click=rätt_svar)

    ui.button("C++", on_click=lambda: ui.navigate.to('/fråga3'))


@ui.page('/fråga3')
def fråga3():

    ui.label("Fråga 3/4")

    ui.label("Vad står VS Code för?")

    def rätt_svar():
        global points
        points += 1
        ui.navigate.to('/fråga4')

    ui.button("Visual Studio Code", on_click=rätt_svar)

    ui.button("Very Simple Code", on_click=lambda: ui.navigate.to('/fråga4'))

    ui.button("Virtual System Code", on_click=lambda: ui.navigate.to('/fråga4'))

@ui.page('/fråga4')
def fråga4():

    def rätt_svar(user_text):
        global points

        if user_text == "2013":
            points += 1

        ui.navigate.to('/klar')

    ui.label("Fråga 4/4")

    ui.label("När startades Storsjögymnasiet")

    user_text = ui.input(label= "Text", placeholder= "Skriv nå")
    ui.button("Klar", on_click= lambda: rätt_svar(user_text.value))


@ui.page('/klar')
def klar():
    ui.label("Klart!")

    ui.label(f'Du fick {points} points!')

    ui.button("Tillbaka till start", on_click=lambda: ui.navigate.to('/secret'))



@ui.page("/secret")
def secret():
    ui.label("Följer du ElectroGamingPC på Twitch?")
    ui.button("JA", on_click=lambda: ui.navigate.to("/de_bra"))
    ui.button("neeee", on_click=lambda: ui.navigate.to("/underkännd"))


@ui.page("/de_bra")
def de_bra():

    ui.label("SUUUUPER 👍👌")
    ui.button("Tillbaka till start", on_click=lambda: ui.navigate.to('/'))



@ui.page("/underkännd")
def underkännd():

    ui.label("underkännd asså...🖕")
    ui.button("Tillbaka till start", on_click=lambda: ui.navigate.to('/'))



ui.run(native=True)
