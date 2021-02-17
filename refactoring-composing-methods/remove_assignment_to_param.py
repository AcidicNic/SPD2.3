# By Kami Bigdely
# Remove assignment to method parameter.
class Distance:
    """Represents the measurement of a distance."""
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value


class Mass:
    """Represents the measurement of a mass."""
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


def calculate_kinetic_energy(mass, distance, time):
    """Returns the kinetic energy calculated from the given data."""
    distance_km = distance
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            distance_value_km = distance.value * 9.461e12
            distance_km = Distance(distance_value_km, "km")
        else:
            print ("unit is Unknown")
            return

    speed = distance_km.value/time # [km per sec]
    mass_kg = mass
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            mass_value_in_kg = mass.value * 1.98892e30 # [kg]
            mass_kg = Mass(mass_value_in_kg, 'kg')
        else:
            print ("unit is Unknown")
            return

    kinetic_energy = 0.5 * mass_kg.value * speed ** 2
    return kinetic_energy

# Test
if __name__ == '__main__':
    mass = Mass(2, "solar-mass")
    distance = Distance(2, 'ly')
    print(calculate_kinetic_energy(mass, distance, 3600e20))
