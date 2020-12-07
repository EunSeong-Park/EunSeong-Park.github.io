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
    pass

  def brrr(self, km):
    '''
    Drive [km]km. You should implement:
      - distance increases as you drive
      - fuel decreases as you use
      - if the fuel is empty, then you cannot go more
        (+ print, "EMPTY!")
    '''
    pass

  def gas_station(self):
    '''
    Re-fuel. Don't worry, it is free.
    '''
    pass
