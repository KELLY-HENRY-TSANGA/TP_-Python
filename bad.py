class Student:
    def __init__(self, name, n1, n2, n3):
        self.name = name
        self.n1, self.n2, self.n3 = n1, n2, n3
        self.average = (n1 + n2 + n3) / 3

class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        print("\n--- Classement Matière 1 ---")
        for s in sorted(self.students, key=lambda x: x.n1, reverse=True):
            print(f"{s.name}: {s.n1}")

    def rank_matter_2(self):
        print("\n--- Classement Matière 2 ---")
        for s in sorted(self.students, key=lambda x: x.n2, reverse=True):
            print(f"{s.name}: {s.n2}")

    def rank_matter_3(self):
        print("\n--- Classement Matière 3 ---")
        for s in sorted(self.students, key=lambda x: x.n3, reverse=True):
            print(f"{s.name}: {s.n3}")

if __name__ == "__main__":
    school_class = SchoolClass()
    
    # Données de test demandées
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    
    # Appels des méthodes de classement
    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()