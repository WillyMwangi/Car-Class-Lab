#You are to create a Car class that can be used to instantiate various vehicles.

#It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.

class Car(object):

#Let the test guide you to building your Car boiler-plate.

    def __init__(self, name='General', model='GM' ,car_type='honda' ):
#The car should be called `General` if no name was passed as an argument
        self.car_type = car_type
        self.model = model        #The car name and model should be a property of the car
        self.name = name
        self.speed = 0

        if name== 'Porshe' or name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def doors(self, num_of_doors):
        pass

    def drive(self, moving_man):
        return moving_man
#The car drive function should return the instance of the Car class
    def drive(self, spd):
        if self.car_type == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = 10 ** spd

        return self
# wheels
    def wheels(self, num_of_wheels):
        return num_of_wheels
