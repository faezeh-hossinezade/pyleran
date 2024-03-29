class Actor:
    def __init__(self,name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def show(self):
        print("Name: ",self.name, "Gender: ",self.gender, "Age: ", self.age)
        