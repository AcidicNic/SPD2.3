# By Kami Bigdely
# Introduce explaining variable (alias extract variable)
# Reference: https://www.researchgate.net/publication/305768969_The_role_of_eye_characteristics_in_facial_beauty_likability_and_attractiveness
# Background: You are a computer engineer trying to sift through many profiles to find
# your soulmate. Unfortunately, there are too many profiles and it's getting tedious. You write a
# python script to scrape profiles info (such as height, age, etc) and images (for image processing)
# to figure out automatically who is attractive to you.  Here is a part of the script:
from math import pi

MIN_IDEAL_EYE_SIZE = 0.45
MIN_IDEAL_EYE_PROPORTION = 0.69
MIN_IDEAL_EYE_ROUNDNESS = 0.59


# assuming you have extracted the following info from the profile's image.
eye_size = 0.47    # [cm^2]
eye_width = 24.2   # [mm]
eye_height = 23.7  # [mm]

iris_width = 20.2  # [mm]
iris_height = 19.7 # [mm]

iris_to_eye_proportion = (pi * iris_width / 2 * iris_height / 2) / eye_size
eye_roundness = eye_height / eye_width

if eye_size > MIN_IDEAL_EYE_SIZE and \
        iris_to_eye_proportion >= MIN_IDEAL_EYE_PROPORTION and \
        eye_roundness >= MIN_IDEAL_EYE_ROUNDNESS:
    print("I’m sorry I wasn’t part of your past, can I make it up by being in your future?")
