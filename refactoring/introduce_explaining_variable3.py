# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    """Returns bool, checking if cooking criteria has been met."""
    # I'm no chef, idk what this number is so idk what to call it :(
    cooked_num = time * temperature * pressure * COOKED_CONSTANT

    if desired_state == 'well-done' and cooked_num >= WELL_DONE:
        return True
    if desired_state == 'medium' and cooked_num >= MEDIUM:
        return True

    return False
