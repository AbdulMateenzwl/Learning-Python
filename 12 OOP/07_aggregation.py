class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    
    def study(self):
        return f"{self.name} is studying"
    
    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"

class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        return f"{student.name} added to {self.name} department"
    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return f"{student.name} removed from {self.name} department"
        return "Student not found in department"
    
    def list_students(self):
        if not self.students:
            return f"No students in {self.name} department"
        return f"Students in {self.name}: " + ", ".join([s.name for s in self.students])

alice = Student("Alice Johnson", "S001")
bob = Student("Bob Smith", "S002")
charlie = Student("Charlie Brown", "S003")

cs_dept = Department("Computer Science")
print(cs_dept.add_student(alice))
print(cs_dept.add_student(bob))
print(cs_dept.list_students())

print(cs_dept.remove_student(alice))
print(cs_dept.list_students())

print(alice.study())

math_dept = Department("Mathematics")
print(math_dept.add_student(alice))
print(math_dept.add_student(charlie))

del cs_dept
print(bob.study())
