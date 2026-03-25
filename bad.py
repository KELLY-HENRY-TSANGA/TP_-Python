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

    from collections.abc import Iterable, Iterator

# 1. Création de l'itérateur pour la Matière 1
class Matter1Iterator(Iterator):
    def __init__(self, students):
        # On trie dès la création de l'itérateur
        self._students = sorted(students, key=lambda x: x.n1, reverse=True)
        self._index = 0

class Matter2Iterator(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda x: x.n2, reverse=True)
        self._index = 0
    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration

class Matter3Iterator(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda x: x.n3, reverse=True)
        self._index = 0
    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration

    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration

# 2. Modification de SchoolClass pour hériter d'Iterable
class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    # Cette méthode rend la classe "bouclable" (for s in school_class)
    def __iter__(self):
        return Matter1Iterator(self.students)


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    
    print("\n--- Parcours Matière 2 ---")
    it2 = Matter2Iterator(school_class.students)
    for s in it2:
        print(f"{s.name}: {s.n2}")

    print("\n--- Parcours Matière 3 ---")
    it3 = Matter3Iterator(school_class.students)
    for s in it3:
        print(f"{s.name}: {s.n3}")

    print("\n--- Parcours via Iterator (Matière 1) ---")
    for student in school_class:
        print(f"{student.name}: {student.n1}")

        def add_fourth_matter(cls):
    orig_init = cls.__init__
    def __init__(self, name, n1, n2, n3, n4=0):
        orig_init(self, name, n1, n2, n3)
        self.n4 = n4
    cls.__init__ = __init__
    return cls

@add_fourth_matter
class Student:
    # ... (garde ton code existant ici)