def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(3))  # Fizz
print(fizz_buzz(5))  # Buzz
print(fizz_buzz(15))  # FizzBuzz
print(fizz_buzz(7))  # 7
