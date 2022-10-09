# Parent class 
class Vehicle:
    def __init__(self,make,model,fuel):
        self.make = make
        #making private parent attributes - use it for child class also
        self.__model = model
        self.__fuel = fuel
    
    # make private method in parent
    def __private_method_parent(self):
        print("THis is private")

# child class
class Car(Vehicle):
    def __init__(self,make,model,fuel,air_conditioning,sunroof):
        # Parent attribute
        Vehicle.make = make
        Vehicle.__model = model
        Vehicle.__fuel = fuel
        
        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    #to access private attibute from parent --> have a public method in child and access it using parent name so you will get the value 
    def show_parent_attribute(self):
        print(Vehicle.make," ",Vehicle.__model," ",Vehicle.__fuel)

    #to access private method from parent --> have a public method and access it using (underscore parentname) _parent name + private mathod parent.
    def show_private_method_of_parent(self):
        self._Vehicle__private_method_parent()

    

myobj = Car("Tesla",2020,"Electric",True,True)
myobj.show_parent_attribute()
myobj.show_private_method_of_parent()





