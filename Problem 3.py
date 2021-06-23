evens = [2,4,6,8]
odds = [1,3,5,7,9]

def checker(num, length):
    if (int(num / 10**(9-length)) % length) == 0:
        return 1
    else:
        return 0

for a in odds:
    for b in evens:
        for c in odds:
            for d in evens:
                for f in evens:
                    for g in odds:
                        for h in evens:
                            for i in odds:
                                test_number = a*(10**8) + b*(10**7) + c*(10**6) + d*(10**5) + 5*(10**4) + f*(10**3) + g*(10**2) + h*10 + i
                                div_value = 0
                                for digit in range(3,10):
                                    if checker(test_number, digit) == 1:
                                        div_value += 1
                                if div_value >= 7:
                                    print(f'{div_value}: {test_number}')


