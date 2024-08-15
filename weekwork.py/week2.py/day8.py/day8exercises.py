# class Rectangle:
#     def __init__(self,width) -> None:
#         self.width = width

#         #getter method = reading = window
#         def get_width(self):
#             return self.width

#         def get_hight(self):
#             return self.height  
        
#         def set_width(self, new_width):
#             self._width =new_width


# r = Rectangle (20,30)
# print("Width is "+str(r.get_width()))
# set_width (50)
# print("Height is "+str(r.getheight()))

#suoper what is super keyword used for?

class MusicalInstruments:
    def __init__(self,) -> None:
        self.name = name

    def play(self):
        return self.name + " is playing"
    
#End

class Guitar(MusicalInstruments):
    def __init__(self, name) -> None:
        super().__init__(name)
        super().play()
#end

class Wilson(MusicalInstruments):
    def __init__(self, name)-> None:
        super().__init__(name)
        super().play()
        
#Creating object
# 

ge = Guitar("Gipsum")  
gr = Guitar ("abc")       


class Employee: # Create employee class
     def __init__(self, employeeId, designation, salary, dateOfJoining) -> None:# Create all the attributes for employee class
        self.employeeId = employeeId
        self.designation = designation
        self.salary = salary
        self.dateOfJoining = dateOfJoining

     def show(self):# create a show method to show details of employee
        return self._employeeId + self._designation + self._salary + + self._dateOfJoining
    
#Setter method
     def set(self, designation, salary):
        self._designation = designation
        self._salary = salary



class Programmer(Employee): 
     def __init__(self, employeeId, designation, salary, dateOfJoining) -> None: 
        super().__init__(employeeId, designation, salary, dateOfJoining)

#Getter Method
     def get_employee(self): # use getter and setter methods to display te information
        print(super().show()) # needed to add print in front of super () and wrap the rest of the etxt in brackets to print.

#Setter Method
     def set_employee(self, designation, salary):
        super().set(designation, salary)
        

#Run - Could not get it to run - could not figure why
empl = Programmer("1", "Software Developer", "4500.50$", "2024-05-05") # This is creating an object.
empl.get_employee() # CALLING ON GETTER METHOD TO SHOW THE INFORMATION