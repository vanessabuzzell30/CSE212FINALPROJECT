# Stack implementation in python
class Stack():
    def __init__(self):
        self.items = []

        # Creating an empty stack
    def push(self, item):
        self.items.append(item)

        # Removing an element from the stack
    def pop(self):
        return self.items.pop()

    def peek(self):
        if not len(self.items) == 0:
            return self.items[-1]

    def get_all(self):
        return self.items


students = Stack()
students.push('John')
students.push('Lily')
students.push('Mark')
students.push('Elijah')
students.push('Layla')
students.push('Joshua')
students.push('Andrew')
students.push('Harper')
students.push('Willow')
students.push('Vanessa')
students.push('Lorraine')

print(students.get_all())

remove_students = students.pop()

print(remove_students)

print(students.get_all())
