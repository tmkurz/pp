import platform
import random
import math

print("Procesor komputera to: ", platform.processor())
print("3 niepowtarzalne liczby ze zbioru 1-10: ", random.sample([i for i in range (1, 11)], 3))
print("Sinus 90 stopni: ", math.sin(math.radians(90)))