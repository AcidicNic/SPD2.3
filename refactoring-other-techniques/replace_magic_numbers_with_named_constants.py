# by Kami Bigdely
# Replace magic numbers with named constanst

# i dont know what this is
SOME_PHYSICS_CONSTANT = 8.9875517923*1e9

# First Section
# Given two point charges, calcualte the electric force exerted on them.
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))

force = SOME_PHYSICS_CONSTANT * q1 * q2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
# what magic number???????????????
num = int(input('Enter an integer number: '))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
