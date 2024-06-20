class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def get_previous(self):
        return self.previous
    def set_previous(self, previous):
        self.previous = previous   
    def get_next(self):
        return self.next
    def set_next(self, next):
        self.next = next 

