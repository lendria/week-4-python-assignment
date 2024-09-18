class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Print out the introduction
        print("Hi, I'm " + self.name + ". I'm " + str(self.age) + " years old and I am " + self.gender + ".")

# Create a person object
person = Person("Anyango", 21, "Male")

# Call the introduce method
person.introduce()
