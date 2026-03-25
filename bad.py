class Student:
    def __init__(self, name, n1, n2, n3):
        self.name = name
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        # Calcul de la moyenne pour l'étape initiale
        self.average = (n1 + n2 + n3) / 3

class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)