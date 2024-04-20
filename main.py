import time

import random

print("What is the highest integer on your die?")

highestint = int(input())

print(" ")

print("What is the lowest integer on your die?")

lowestint = int(input())

print(" ")

print("Rolling die...")

time.sleep(1)

print(random.randrange(lowestint, highestint))

time.sleep(5)