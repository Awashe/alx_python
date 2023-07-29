import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number

quotient, remainder = divmod(number, 10)
last_digit = remainder
if number < 0:
    last_digit = -last_digit
if number >= 0:
    last_digit = last_digit
if number == 0:
  last_digit = 0
if last_digit > 5:
    print(f"last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is 0")
else:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")
