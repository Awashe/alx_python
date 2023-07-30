numbers = []
for i in range(0, 100):
  two_digit = "{0:02}".format(i)
  numbers.append(two_digit)

print(", ".join(numbers))
