def sum_digit(num):
    if num < 10:
        return num;
    return (num % 10) + sum_digit(num // 10)

n = int(input())
print(sum_digit(n))
