from ListaDobleEnlazada import ListaDobleEnlazada
from Athlete import Athlete
myList = ListaDobleEnlazada()
option = 0

def int_validation(number):
    try:
        number = int(number)
        return True
    except:
        return 

while option != 9:
    option = int(input("\n======= Menu =======\n"
                       "Select an option:\n"
                       "1. Add athlete\n" 
                       "2. Search athete\n" 
                       "3. Show positions\n" 
                       "4. Modify athlete\n" 
                       "5. Delete athlete\n" 
                       "6. Run\n"
                       "7. Pass competitor\n"
                       "8. Race\n"
                       "9. Salir\n"))
    
    match option:
        case 1:
            name = input("Type the athlete's name: ")
            number = input("Enter the athlets's number: ")
            if int_validation(number):
                athlete = Athlete(name, number)
                myList.add_last(athlete)
            else:
                print("The athlete's number must be an integer. Try again. ")
        
        case 2:
            number =  input("Enter the athlets's number to search: ")
            if int_validation(number):
                myList.search(number)
                if myList.search(number):
                    print(f"The athlete {number} is in the race.")
                elif not myList.search(number):
                    print(f"The athlete {number} isn't in the race.")
            else:
                print("The athlete's number must be an integer. Try again. ")    
       
        case 3:
            print(myList.show())
        
        case 4:
            number = input("Enter the athlets's number to modify: ")
            if int_validation(number):
                if myList.modify(number):
                    print("The Athlete's name has been changed")
                else: 
                    print("There isn't any athlete with the entered number")
            else:
                print("The athlete's number must be an integer. Try again. ")
        
        case 5:
            number = input("Enter the athlets's number to delete: ")
            if int_validation(number):
                myList.delete(number)
            else:
                print("The athlete's number must be an integer. Try again. ")
        case 6:
            myList.run()
        case 7: 
            number = input("Enter the athlets's number: ")
            if int_validation(number):
                myList.PassCompetitor(number)
            else:
                print("The athlete's number must be an integer. Try again. ")
        case 8:
            laps = input("Enter the number of laps: ")
            if int_validation(laps):
                myList.race(int(laps))
            else:
                print("Number of laps must be an integer. Try again.")
                
            
            
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
""" cedula = int(input("Digite la cedula: "))
            nombre = input("Digite el nombre: ")
            edad = int(input("Digite la edad: "))
            empleado = Empleado(cedula, nombre, edad)
            posicion = int(input("¿Desea agregarlo al inicio (1) o al final (2)?"))
            if posicion == 1:
                myList.agregar_inicio(empleado)
            elif posicion == 2:
                myList.agregar_final(empleado)
            else:
                print("opción inválida")
        case 2: 
            print(myList.mostrar())
        case 3:
            dato = int(input("Digite la cedula de la persona que desea modificar: "))
            if myList.modificar(dato):
                print("Persona modificada.")
            else:
                print("Persona no encontrada. No se puede modificar")
        case 4:
            dato = int(input("Digite la cédula de la persona que desea buscar: "))
            if myList.buscar(dato):
                print("Persona encontrada")
            else:
                print("Persona no encontrada")
        case 5:
            dato = int(input("Digite la cedula de la persona que desea eliminar: "))
            if myList.eliminar(dato):
                print("Persona eliminada.")
            else:
                print("Error. Persona no eliminada")
        case 6:
            print("Saliendo del programa...")
        case _:
            print("Opción inválida")"""