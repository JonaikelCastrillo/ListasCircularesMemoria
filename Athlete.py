class Athlete:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_number(self):
        return self.number
    def set_number(self, number):
        self.number = number   
    def __str__(self):
        return f"Name: {self.name}, Number: {self.number} \n"
    