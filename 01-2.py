import math

def calc_fuel(value):
    return math.floor((int(value) / 3)) - 2 


lines = [line.rstrip('\n') for line in open('input01.txt')]
# lines = ['1969']
# print(lines)
res=0
for line in lines: 
    fuel = calc_fuel(line)
    res += fuel
    while fuel > 0:
        fuel = calc_fuel(fuel)
        if(fuel > 0):
            res += fuel


print(res)


assert(res == 966)