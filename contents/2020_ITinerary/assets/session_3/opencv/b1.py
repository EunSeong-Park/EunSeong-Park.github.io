class Car:
    def __init__(self, name, mileage, max_fuel):
        self.name = name
        self.mileage = mileage
        self.max_fuel = max_fuel
        self.fuel = self.max_fuel
        self.dist = 0

    def status(self):
        ''' Show the current status of the car
        it should be called after brrr() and gas_statation()

        <<< Template >>>
        Car name: [car name]
         Mileage: [mileage]km/L
            Fuel: [Current fuel]L / [Max fuel]L
        Distance: [Total Distance]km

        if fuel < 20 %, print this:
        "WARNING: remaining fuel is too low"
        '''
        print("Car name: " + self.name +
            "\n Mileage: " + str(self.mileage) + "km/L" +
            "\n    Fuel: " + str(self.fuel) + "L / " + str(self.max_fuel) + "L" +
            "\nDistance: " + str(self.dist) + "km")
        if self.fuel / self.max_fuel <= 0.2:
            print("WARNING: remaining fuel is too low")
        print()

    def brrr(self, km): # km
        '''
        Drive [km]km. You should implement:
          - distance increases as you drive
          - fuel decreases as you use
          - if the fuel is empty, then you cannot go more
            (+ print, "EMPTY!")
        '''
        empty = False
        for i in range(km):
            if self.fuel > 1 / self.mileage:
                self.dist += 1
                self.fuel -= 1 / self.mileage
            else:
                empty = True
                break
        self.status()
        if empty: print("EMPTY!")

    def gas_station(self):
        '''
        Re-fuel. Don't worry, it is free.
        '''
        self.fuel = self.max_fuel
        self.status()

k3 = Car("BMW", 16, 50)
k3.brrr(400)


