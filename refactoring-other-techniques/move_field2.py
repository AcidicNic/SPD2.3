# Kami Bigdely
# Move Field

class Car:
    """Represents a car."""
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        for w in wheels:
            w.set_car(self)
        self.cabin = cabin
        self.fuel_tank = fuel_tank


class Wheel:
    """Represents the wheel of a car."""
    def __init__(self, car=None, wheel_location=None, tpms=None):
        self.car = car
        self.wheel_location = wheel_location
        self.tpms = tpms  # Tire Pressure Monitoring System.

    def install_tire(self):
        """Installs a tire."""
        print('remove old tube.')
        print(f'cleaned tpms: {self.tpms.get_serial_number()}.')
        print('installed new tube.')

    def read_tire_pressure(self):
        """Returns the tire pressure."""
        return self.tpms.get_pressure()

    def set_car(self, car):
        """Set 'self.car'."""
        self.car = car

    def set_tpms(self, tpms):
        """Set 'self.tpms'."""
        self.tpms = tpms


class Tpms:
    """Represents a Tire Pressure Monitoring System."""
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]

    def get_pressure(self):
        """Returns the pressure."""
        return 3

    def get_serial_number(self):
        """Returns serial number."""
        return self.serial_number


class Engine:
    """Represents the engine of a car."""
    def __init__(self):
        pass


class FuelTank:
    """Represents the fuel tank of a car."""
    def __init__(self):
        pass


class Cabin:
    """Represents the cabin of a car."""
    def __init__(self):
        pass

if __name__ == '__main__':
    engine = Engine()
    wheels = [Wheel(None, 'front-right', Tpms(983408543)),
                Wheel(None, 'front-left', Tpms(4343083)),
                Wheel(None, 'back-right', Tpms(23654835)),
                Wheel(None, 'back-left', Tpms(3498857))]

    cabin  = Cabin()
    fuel_tank = FuelTank()

    my_car = Car(engine, wheels, cabin, fuel_tank)
