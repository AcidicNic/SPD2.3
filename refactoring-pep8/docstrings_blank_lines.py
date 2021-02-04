class OnBoardTemperatureSensor:
    """Represents a temperature sensor."""
    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def read_voltage(self):
        """Returns the voltage."""
        return 2.7

    def get_temperature(self):
        """Returns the temperature in Celcius."""
        return self.read_voltage() * self.VOLTAGE_TO_TEMP_FACTOR


class CarbonMonoxideSensor:
    """Represents a carbon monoxide sensor."""
    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Returns the current carbon monoxide level."""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = self.convert_voltage_to_carbon_monoxide_level(
            sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Returns the current voltage."""
        # In real life, it should read from hardware.
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """Calculates a carbon monoxide level using 'voltage' and
        'temperature'.
        """
        return voltage * self.VOLTAGE_TO_CO_FACTOR * temperature


class DisplayUnit:
    """Represents a display unit."""
    def __init__(self):
        self.string = ''

    def display(self, msg):
        """Prints 'msg' to the display."""
        print(msg)


class CarbonMonoxideDevice():
    """Represents a carbon monoxide sensor with a display."""
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor
        self.display_unit = display_unit

    def display(self):
        """Prints the carbon monoxide level to 'self.display_unit's display."""
        msg = 'Carbon Monoxide Level is : ' \
            f'{self.carbonMonoxideSensor.get_carbon_monoxide_level():.2f}'
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()
