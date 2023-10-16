class Car:
    color = None
    fuel = None
    maxspeed = None

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def typeInfo(self):
        print(" Color:", myCar.color, "\n", "Fuel:", myCar.fuel, "\n", "Max speed:", myCar.maxspeed)


class DiffCar:
    color = None
    fuel = None
    maxspeed = None

    def typeInfo(self):
        print(" Color:", myDiffCar.color, "\n", "Fuel:", myDiffCar.fuel, "\n", "Max speed:", myDiffCar.maxspeed)


myCar = Car()  # первый class
myCar.color = 'red'
myCar.fuel = 50
myCar.maxspeed = 160
myCar.typeInfo()
myCar.go()
myCar.turn()
myCar.stop()

myDiffCar = DiffCar()  # второй class
myDiffCar.color = 'green'
myDiffCar.fuel = 70
myDiffCar.maxspeed = 130
myDiffCar.typeInfo()
