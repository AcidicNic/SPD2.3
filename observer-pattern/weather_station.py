from prettytable import PrettyTable

def get_min_max_avg(num_list):
    """Returns the (min, max, avg) of 'num_list'."""
    return (round(min(num_list), 1), round(max(num_list), 1),
        round(sum(num_list)/len(num_list), 1))


class Subject:
    """Subject superclass."""

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        """Adds 'observer' to 'self.observers'."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Removes 'observer' from 'self.observers'."""
        self.observers.remove(observer)

    def notify_observers(self):
        """Updates measurements on all observers."""
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)


class Observer:
    """The observer superclass."""

    def __init__(self, weather_data):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        """Updates the temperature, humidity, and pressure properties.
        Updates the display."""
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()


class WeatherData(Subject):
    """Holds all of the data from the weather station.
    Distributes data to observers"""

    def measurements_changed(self):
        """Notifies observers that the measurements have been updated."""
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        """Sets the temperature, humidity, and pressure properties.
        Notifies oberservers of these changes."""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()


class CurrentConditionsDisplay(Observer):
    """A display for the current weather conditions."""

    def display(self):
        """Prints the current conditions."""
        conditions = PrettyTable(title="Current Conditions",
                     field_names=["Temperature", "Humidity", "Pressure"])

        conditions.add_row([f"{self.temerature:.1f}°F", f"{self.humidity:.1f}%",
                            f"{self.pressure:.1f}"])
        print(conditions)


class ForecastDisplay(Observer):
    """A display for the current weather forecast."""

    def get_forecast(self):
        """Returns the forecasted (temperature, humidity, pressure)."""
        f_temp = self.temerature + 0.11 * self.humidity + 0.2 * self.pressure
        f_humi = self.humidity - 0.9 * self.humidity
        f_pres = self.pressure + 0.1 * self.temerature - 0.21 * self.pressure
        return (round(f_temp, 1), round(f_humi, 1), round(f_pres, 1))

    def display(self):
        """Prints the current forecasted weather."""
        forcasted_weather = self.get_forecast()

        forecast = PrettyTable(field_names=["***", "Forecast"])
        forecast.add_row(["Temperature", f"{forcasted_weather[0]}°F"])
        forecast.add_row(["Humidity", f"{forcasted_weather[1]}%"])
        forecast.add_row(["Pressure", f"{forcasted_weather[2]}"])

        print(forecast)


class StatisticsDisplay(Observer):
    """A display for the current weather statistics."""

    def __init__(self, weather_data):
        super().__init__(weather_data)
        self.temerature_list = []
        self.humidity_list = []
        self.pressure_list = []

    def update(self, temperature, humidity, pressure):
        """Updates temerature_list, humidity_list, pressure_list, temperature,
        humidity, pressure properties, and the display."""
        self.temerature_list.append(temperature)
        self.humidity_list.append(humidity)
        self.pressure_list.append(pressure)
        super().update(temperature, humidity, pressure)

    def display(self):
        """Prints the current weather statistics."""
        temp_stats = get_min_max_avg(self.temerature_list)
        humi_stats = get_min_max_avg(self.humidity_list)
        pres_stats = get_min_max_avg(self.pressure_list)

        stats = PrettyTable(title="Statistics",
                            field_names=["***", "min", "max", "avg"])

        stats.add_row(["Temperature", f"{temp_stats[0]}°F",
                       f"{temp_stats[1]}°F", f"{temp_stats[2]}°F"])
        stats.add_row(["Humidity", f"{humi_stats[0]}%",
                       f"{humi_stats[1]}%", f"{humi_stats[2]}%"])
        stats.add_row(["Pressure", pres_stats[0], pres_stats[1],
                       pres_stats[2]])
        print(stats)


class WeatherStation:
    """Represents a weather station."""

    def main(self):
        """Tests the functionality of the code above."""
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.set_measurements(80, 65, 30.4)
        weather_data.set_measurements(82, 70, 29.2)
        weather_data.set_measurements(78, 90, 29.2)

        weather_data.remove_observer(current_display)
        weather_data.remove_observer(statistics_display)
        weather_data.remove_observer(forecast_display)
        weather_data.set_measurements(120, 100, 1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
