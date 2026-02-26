from nicegui import ui

todos = []
import ast

#ladda tidigare data
try:
    with open("todo_data.txt", "r", encoding="utf-8") as f:
        data = ast.literal_eval(f.read())
        todos = data["todos"]
except:
    pass


dark = ui.dark_mode()

switch = ui.switch('smek mej')
dark.bind_value(switch) 

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
    
    with open("todo_data.txt", "w", encoding="utf-8") as f:
        f.write(str({"todos": todos, "todos": todos}))

for task in todos:
        with list_container:
            ui.label(task).classes("border p-2 rounded w-80 bg-purple-200")

ui.button("Lägg till", on_click=add_task)




ui.run(native=True)
