test_number = 10 ** 4
answer = 10 ** 4 + 1

while test_number < 10**5:
    sum_of_digits = sum(int(digit) for digit in str(test_number))
    divided_by_digits = test_number / sum(int(digit) for digit in str(test_number))
    if divided_by_digits < answer:
        answer = divided_by_digits
        print(f'{test_number}/{sum_of_digits} = {divided_by_digits}')
    test_number += 1
