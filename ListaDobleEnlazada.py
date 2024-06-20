from Node import Node
from Athlete import Athlete
import random

        
class ListaDobleEnlazada:
    def __init__(self):
        self.head = None 
        self.latest = None
       
    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  
            self.latest = new_node
        else:
            new_node.previous = self.latest
            self.latest.next = new_node
            self.latest = new_node
            self.latest.next = self.head
            self.head.previous = self.latest 
            
    def modify(self, data):
        current_node = self.head
        flag = False
        modified = False
        while current_node != None and modified == False:
            if current_node.data.get_number() == data:
                number = current_node.data.get_number()
                new_name = input("Type the new athlete's name: ")
                athlete = Athlete(new_name, number)
                current_node.set_data(athlete)
                flag = True
                modified = True
            current_node = current_node.next
        return flag
               
    def delete(self, data):
        current = self.head
        end = False
        deleted = False
        while current and end == False:
            if current.data.get_number() == data:
                if current.previous:
                    current.previous.next = current.next
                if current.next:
                    current.next.previous = current.previous
                if current == self.head:
                    self.head = current.next
                if current == self.latest:
                    self.latest = current.previous
                current.previous = None #rompe los enlaces del atleta que se está eliminando con sus nodos vecinos.
                current.next = None
                print("Athlete deleted succesfully")
                deleted = True
                return
            current = current.next
            if current == self.head:
                end = True
        if deleted == False:
            print("The athlete isn't in the race ")
    def show(self):
        current = self.head
        end = False
        while current != None and end == False:
            behind = ""
            front = ""
            if current.previous != None:
                behind = current.previous.data.get_number()
            if current.next != None:
                front = current.next.data.get_number()
            print(f"Behind athlete {current.data.get_number()} comes {behind} and in front of {current.data.get_number()} comes {front}")
            current = current.next
            if current == self.head:
                end = True
        
    
    def search(self, data):
        current_node = self.head
        flag = False
        end = False
        while current_node != None and end == False:
            if current_node.data.get_number() == data:
                flag = True
                end = True
            current_node = current_node.next
            if current_node == self.head:
                end = True
        return flag
    
    def search_node(self, data):
        current_node = self.head
        node = None
        end = False
        while current_node != None and end == False:
            if current_node.data.get_number() == data:
                end = True
                node = current_node
                print(node.data)
            current_node = current_node.next
            if current_node == self.head:
                end = True
        return node
        
    
    def run(self):
        if self.head is None or self.head == self.latest:
            return
        current = self.latest
        while current != self.head:
            temp = current.data
            current.data = current.previous.data
            current.previous.data = temp
            current = current.previous

        # Después de realizar el desplazamiento, se ajusta el head y el latest
        self.head.previous = self.latest
        self.latest.next = self.head
        
    def PassCompetitor(self, athlete1):
        athlete = self.search_node(athlete1)
        next_athlete = athlete.next
    
        if athlete is None:
            print("This athlete isn't in the run")
            return
        if athlete == self.latest:
            self.run()  
            temp_data = self.head.data
            self.head.data = self.head.next.data
            self.head.next.data = temp_data  
        else:
            temp_data = athlete.data
            athlete.data = next_athlete.data
            next_athlete.data = temp_data  
        
    def race(self, laps):
        if self.head is None:
            print("There are no athletes. Add them first.")
            return
        
        current = self.head
        total_nodes = 0
        end = False
        while current and not end:
            total_nodes += 1
            current = current.next
            if current == self.head:
                end = True
        
        for x in range(total_nodes):
            random_index = random.randint(0, total_nodes - 1) 
            current = self.head
            for x in range(random_index):
                current = current.next
            temp = current.data
            current.data = self.head.data
            self.head.data = temp
            
        print("\nOrder of athletes at the start of the race (randomly sorted):")
        self.show()
        print()
    
        for _ in range(laps):
            self.run()
    
        print(f"""The winner of the race is:
{self.head.data} """)
            
        
    