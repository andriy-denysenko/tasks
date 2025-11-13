import math

def infected(days):
    infected_count = 0
    for i in range(days + 1):
        print(f'Day {i}')
        if i == 0:
            infected_count = 1
        elif i % 3 == 0:
            infected_count *= 2
            patched = math.ceil(infected_count / 100 * 20)
            infected_count -= patched
        else:
            infected_count *= 2
    return infected_count

args = [1, 3, 8, 17, 25]
ress = [2, 6, 152, 39808, 5217638]
for i in range(len(args)):
    print(f'arg = {args[i]}; infected = {infected(args[i])} == result = {ress[i]}')
    print('----------------------------------------------------------------------')
    print()