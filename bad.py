from collections.abc import Iterable, Iterator

# --- DÉCORATEUR (Question 7) ---
def add_fourth_matter(cls):
    orig_init = cls.__init__
    def __init__(self, name, n1, n2, n3, n4=0):
        orig_init(self, name, n1, n2, n3)
        self.n4 = n4
    cls.__init__ = __init__
    return cls

@add_fourth_matter
class Student:
    def __init__(self, name, n1, n2, n3):
        self.name = name
        self.n1, self.n2, self.n3 = n1, n2, n3
        self.average = (n1 + n2 + n3) / 3

# --- LES ITÉRATEURS (Questions 4, 5 et 8) ---
class Matter1Iterator(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda x: x.n1, reverse=True)
        self._index = 0
    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration

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

class Matter4Iterator(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda x: x.n4, reverse=True)
        self._index = 0
    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration

# --- LA CLASSE PRINCIPALE (Question 9 - Singleton inclue) ---
class SchoolClass(Iterable):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls)
            cls._instance.students = []
        return cls._instance

    def add_student(self, student):
        self.students.append(student)

    # --- MÉTHODES DE TRI (Question manquante) ---
    def rank_matter_1(self):
        print("\n--- Classement Matière 1 (Méthode) ---")
        for s in sorted(self.students, key=lambda x: x.n1, reverse=True):
            print(f"{s.name}: {s.n1}")

    def rank_matter_2(self):
        print("\n--- Classement Matière 2 (Méthode) ---")
        for s in sorted(self.students, key=lambda x: x.n2, reverse=True):
            print(f"{s.name}: {s.n2}")

    def rank_matter_3(self):
        print("\n--- Classement Matière 3 (Méthode) ---")
        for s in sorted(self.students, key=lambda x: x.n3, reverse=True):
            print(f"{s.name}: {s.n3}")

    def __iter__(self):
        return Matter1Iterator(self.students)

# --- BLOC MAIN (Appels de test) ---
if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    school_class.add_student(Student('New', 10, 10, 10, 18)) # Test Matière 4

    # Test des méthodes de tri (Question demandée)
    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()

    # Test des Itérateurs
    print("\n--- Test Itérateur Matière 4 ---")
    for s in Matter4Iterator(school_class.students):
        print(f"{s.name}: {s.n4}")