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
        # super() is used to access the parent attributes 
        super(Car,self).__init__(make,model,fuel)

        self.air_cinditioning = air_conditioning
        self.sunroof = sunroof
        
        
       
    
    

myobj = Car("Tesla",2020,"Electric",True,True)
#we can just access the private method parent directly usinh (underscore parent name)_Vehicle + private method parent
myobj._Vehicle__private_method_parent()






