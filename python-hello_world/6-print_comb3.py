for i in range(10):
    for j in range(i+1,10):
        print("{0}{1}, ".format(i,j), end="")
for i in range(1,9):
    for j in range(i+1,10):
        print("{0}{1}, ".format(i,j), end="")
print("89")
'''
numbers = ""
for i in range(0, 100):
  two_digit = "{0:02}".format(i)
  numbers += two_digit + ", "

print(numbers[:-2])
'''