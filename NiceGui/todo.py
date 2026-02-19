from nicegui import ui

todos = []

dark = ui.dark_mode()

switch = ui.switch('smek mej')
dark.bind_value(switch)  # <-- DETTA är det rätta

ui.label("ToDo List📝").classes("text-3xl")

user_text = ui.input(label="ToDo +", placeholder="Skriv nå o lägga till")

list_container = ui.column()

def add_task():
    todos.append(user_text.value)
    user_text.value = ""
    list_container.clear()

    for task in todos:
        with list_container:
            ui.label(task).classes("border p-2 rounded w-80 bg-purple-200")

ui.button("Lägg till", on_click=add_task)

ui.run(native=True)
