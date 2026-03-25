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

        # Ajoute ceci tout à la fin de bad.py
if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    print("Données de test ajoutées.")