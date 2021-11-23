import functools

numbers = ["10", "68", "75", "7", "21", "12"]

numbers.sort(key=functools.cmp_to_key(lambda x, y: int(x+y)-int(y+x)), reverse=True)
numbers = ''.join(numbers)

print(numbers)
