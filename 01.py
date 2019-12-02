import math

def calc_fuel(value):
    return math.floor((int(value) / 3)) - 2 


lines = [line.rstrip('\n') for line in open('input01.txt')]
# print(lines)
res=0
for line in lines:
    res += calc_fuel(line)

print(res)
# print(calc_fuel(14))


assert(calc_fuel(12) == 2)
assert(calc_fuel(14) == 2)
assert(calc_fuel(1969) == 654)
assert(calc_fuel(100756) == 33583)
