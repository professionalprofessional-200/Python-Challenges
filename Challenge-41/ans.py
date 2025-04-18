class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Example usage
person1 = Person("Alice", 30)
person1.display_details()
