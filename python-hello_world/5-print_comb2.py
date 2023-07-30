numbers = ""
for i in range(0, 100):
  two_digit = "{0:02}".format(i)
  numbers += two_digit + ", "

print(numbers[:-2])