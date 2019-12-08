# prog = ['1','0','0','0','99']
# prog = ['1','1','1','4','99','5','6','0','99']
# prog = ['2','3','0','3','99']
# prog = ['2','4','4','5','99','0']

original_prog = open('input02.txt').read().rstrip('\n').split(',')


# prog[1] = '12'
# prog[2] = '2'


def check_opcode(start, prog):
    if prog[start] == '1':
        res_sum = int(prog[int(prog[start + 1 ])]) + int(prog[int(prog[start + 2])])
        res = True
    if prog[start] == '2':
        res_sum = int(prog[int(prog[start + 1 ])]) * int(prog[int(prog[start + 2])])
        res = True
    if prog[start] == '99':
        return False
    prog[int(prog[start + 3])] = str(res_sum)
    return res


def gravity(input, noun, verb):
    s = 0
    input[1] = noun
    input[2] = verb
    while True:
        r = check_opcode(s, input)
        s += 4
        if not r:
            break
    
    return int(input[0])


# noun = 1
# verb = 1
result = 0

# while result != 19690720:
for noun in range(0, 99):
    for verb in range(0, 99):
        p = original_prog.copy()
        result = gravity(p, noun, verb)
        # if result > 19600000:
            # print(result)
        if result == 19690720:
            print(100 * noun + verb)
        # result = 100 * noun + verb


# if 100*noun+verb == 19690720:
#     print(100 * noun + verb)
