src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

resalt = [num for num in src if src.count(num) <= 1]  
print(resalt)
