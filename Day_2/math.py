import math
def valu(r,h):
  return math.exp(h)+math.log((r-1),10)



r=int(input('enter a r'))
h=int(input('enter a h'))

a=valu(r,h)

print(f'the values is {a:.2f} ')



