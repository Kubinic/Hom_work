def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


print(list(odd_nums(963)))