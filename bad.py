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
        # On trie la liste par la note n1 (index 0 ou attribut n1)
        for s in sorted(self.students, key=lambda x: x.n1, reverse=True):
            print(f"{s.name}: {s.n1}")

if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    
    
    school_class.rank_matter_1()