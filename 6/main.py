# Array (lista) studenata:
# Svaki student: name: "Toma", score 0-100, active: true/false
from time import process_time

students = [
    {
        "name": "Toma",
        "score": 99,
        "active": True
    },
    {
        "name": "Marija",
        "score": 49,
        "active": False

    },
    {
        "name": "Milos",
        "score": 85,
        "active": True
    }
]

# Ako ke score studenta (ovo vazi samo za aktivne studente)
# od 80 do 100 -> "grade": "A"
# od 60 do 80 -> "grade": "B"
# od 40 do 60 -> "grade": "C"
# od 20 do 40 -> "grade": "D"
# < 20 -> "grade": "F"

for student in students:
    if student["active"] and 80 < student["score"] <= 100:
        student["grade"] = "A"
    elif student["active"] and 60 < student["score"] <= 80:
        student["grade"] = "B"
    elif student["active"] and 40 < student["score"] <= 60:
        student["grade"] = "C"
    elif student["active"] and 20 < student["score"] <= 40:
        student["grade"] = "D"
    elif student["active"] and student["score"] <= 20:
        student["grade"] = "F"

print(students)