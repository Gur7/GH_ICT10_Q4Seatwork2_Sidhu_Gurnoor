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
    Classmate("Joe", "Emerald", "Math"),
    Classmate("Erin", "Emerald", "Science"),
    Classmate("Caitlyn", "Emerald", "English"),
    Classmate("Kyla", "Emerald", "Filipino"),
    Classmate("Oscar", "Emerald", "History"),
    Classmate("Clarrise", "Emerald", "Math"),
    Classmate("Thomas", "Emerald", "Science"),
    Classmate("Ivan", "Emerald", "English"),
    Classmate("Aurelia", "Emerald", "Filipino"),
    Classmate("Lan", "Emerald", "History"),
    Classmate("Fran", "Emerald", "Math"),
    Classmate("Kiesha", "Emerald", "Science"),
    Classmate("Hikari", "Emerald", "English"),
    Classmate("Ashe", "Emerald", "Filipino"),
    Classmate("Juanico", "Emerald", "No fav Subject"),
    Classmate("Julia", "Emerald", "Math"),
    Classmate("James", "Emerald", "Science"),
    Classmate("Sophia", "Emerald", "English"),
    Classmate("Yciar", "Emerald", "Filipino"),
    Classmate("Gino", "Emerald", "History"),
    Classmate("Gurnoor", "Emerald", "Math"),
    Classmate("Lia", "Emerald", "Nothing but air"),
    Classmate("Erich", "Emerald", "English"),
    Classmate("Zaragoza", "Emerald", "Filipino")
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
