import js
from pyscript import display


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

classmates = [
    Classmate("Juanico", "Emerald", "Math"),
    Classmate("Gino", "Emerald", "Science"),
    Classmate("Oscar", "Emerald", "English"),
    Classmate("Thomas", "Emerald", "Filipino"),
    Classmate("Angela", "Emerald", "History")
]

def show_list(event=None):
    output = "<b> Classmate List</b><ul>"
    for cm in classmates:
        output += f"<li>{cm.introduce()}</li>"
    output += "</ul>"

    js.document.getElementById("output").innerHTML = output

def add_classmate(event=None):
    name = js.document.getElementById("name_input").value
    section = js.document.getElementById("section_input").value
    favorite_subject = js.document.getElementById("subject_input").value

    if name and section and favorite_subject:
        classmates.append(Classmate(name, section, favorite_subject))

        js.document.getElementById("name_input").value = ""
        js.document.getElementById("section_input").value = ""
        js.document.getElementById("subject_input").value = ""

        js.document.getElementById("output").innerHTML = f"<p>{name} added successfully!</p>"
    else:
        js.document.getElementById("output").innerHTML = "<p>Please fill in all fields.</p>"

js.window.add_classmate = add_classmate
js.window.show_list = show_list