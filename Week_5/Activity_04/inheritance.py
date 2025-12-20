#Person Class (Parent Class)
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def describe(self):
        return f"Person({self.id}, {self.name})"

#Student Class inheried from Person
class Student(Person):
    def __init__(self, id, name, student_id):
        super().__init__(id, name)
        self.student_id = student_id

    def describe(self):
        return f"Student({self.id}, {self.name}, {self.student_id})"

#Staff Class inheried from Person
class Staff(Person):
    def __init__(self, id, name, staff_id, tax_num):
        super().__init__(id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def describe(self):
        return f"Staff({self.id}, {self.name}, {self.staff_id}, {self.tax_num})"

#General Class inherited from Staff
class General(Staff):
    def __init__(self, id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def describe(self):
        return f"General({self.id}, {self.name}, {self.staff_id}, {self.tax_num}, {self.rate_of_pay})"

# Academic Class inherited from Staff
class Academic(Staff):
    def __init__(self, id, name, staff_id, tax_num, publications):
        super().__init__(id, name, staff_id, tax_num)
        self.publications = publications

    def describe(self):
        return f"Academic({self.id}, {self.name}, {self.staff_id}, {self.tax_num}, {self.publications})"

def main():
    # Create an Academic staff member
    academic_staff1 = Academic(
        "12345",                 # id
        "Nirmal Chathura",        # name
        "11111",                 # staff_id
        "202-124-234-345",       # tax_num
        1                        # publications
    )

    # Create a General staff member
    general_staff1 = General(
        "67890",                 # id
        "Alice Brown",           # name
        "22222",                 # staff_id
        "303-555-888-999",       # tax_num
        50000                    # rate_of_pay
    )

    # Create a Student
    student1 = Student(
        "99999",                 # id
        "Bob Smith",             # name
        "STU-101"                # student_id
    )

    # Print descriptions
    print(academic_staff1.describe())
    print(general_staff1.describe())
    print(student1.describe())


if __name__ == "__main__":
    main()
