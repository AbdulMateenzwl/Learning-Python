class Student:
    def __init__(self, name, student_id, gpa) -> None:
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def __str__(self) -> str:
        return f"{self.name} (ID: {self.student_id}, GPA: {self.gpa})"

    def __repr__(self) -> str:
        return f"Student('{self.name}', {self.student_id}, {self.gpa})"

    def __eq__(self, other) -> bool:
        """Define equality based on student_id"""
        if not isinstance(other, Student):
            return False
        return self.student_id == other.student_id

    def __ne__(self, other) -> bool:
        """Not equal (usually automatically derived from __eq__)"""
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        """Less than - compare by GPA"""
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa < other.gpa

    def __le__(self, other) -> bool:
        """Less than or equal"""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other) -> bool:
        """Greater than"""
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa > other.gpa

    def __ge__(self, other) -> bool:
        """Greater than or equal"""
        return self.__gt__(other) or self.__eq__(other)

    def __hash__(self) -> int:
        """Make object hashable (required when defining __eq__)"""
        return hash(self.student_id)


# Usage examples
student1 = Student("Alice", 123, 3.8)
student2 = Student("Bob", 124, 3.6)
student3 = Student("Alice Smith", 123, 3.9)  # Same ID as student1

# Equality comparison
print(student1 == student2)  # False (different IDs)
print(student1 == student3)  # True (same ID)
print(student1 != student2)  # True

# Ordering comparisons
print(student1 > student2)   # True (3.8 > 3.6)
print(student1 < student2)   # False
print(student1 >= student2)  # True

# Can now sort students by GPA
students = [student2, student1, student3]
sorted_students = sorted(students)  # Sorts by GPA using __lt__
for student in sorted_students:
    print(student)

print(repr(student1))

# Can use in sets and as dict keys (because of __hash__)
student_set = {student1, student2, student3}
# 2 (student1 and student3 are equal)
print(f"Unique students: {len(student_set)}")
