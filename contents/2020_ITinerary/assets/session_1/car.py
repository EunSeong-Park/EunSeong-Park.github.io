# skeleton

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
    print("Car name: " + self.name)
    print("Mileage:  " + str(self.mileage) + "km/L")
    print("Fuel:     " + str(self.fuel) + "L" + " / " + str(self.max_fuel) + "L")
    print("Distance: " + str(self.dist) + "km")

  def brrr(self, km):
    '''
    Drive [km]km. You should implement:
      - distance increases as you drive
      - fuel decreases as you use
      - if the fuel is empty, then you cannot go more
        (+ print, "EMPTY!")
    '''
    for i in range(km):
        if self.fuel > 1 / self.mileage: # it can go
            self.fuel = self.fuel - 1 / self.mileage
            self.dist = self.dist + 1
        else: # it cannot go
            break
    self.status()

  def gas_station(self):
    self.fuel = self.max_fuel
    self.status()

benz = Car("Benz", 25, 100)
benz.brrr(10000)
benz.gas_station()
benz.brrr(1000)
benz.gas_station()
