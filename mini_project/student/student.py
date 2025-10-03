class students:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}"

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}"