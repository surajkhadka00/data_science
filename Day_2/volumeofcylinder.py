import math
def volume(r,h):
    return math.pi*r**2*h
r=int(input("enter a radius"))
h=int(input("enter a height"))
print(f"volume os cylender is:{volume(r,h):.2f}meter cude")