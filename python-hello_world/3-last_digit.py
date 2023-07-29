import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number

quotient, remainder = divmod(number, 10)
last_digit = remainder

if number >= 0:
    last_digit = last_digit
else:
    last_digit = -last_digit

if number == 0:
    last_digit = 0

message = "Last digit of {} is {} ".format(number, last_digit)

if last_digit > 5:
    message += "and is greater than 5"
elif last_digit == 0:
    message += "and is 0"
else:
    message += "and is less than 6 and not 0"

print(message)