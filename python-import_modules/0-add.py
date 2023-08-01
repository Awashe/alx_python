a = 1
b = 2

add_module = __import__('add_0')

result = add_module.add(a, b)

if __name__ == '__main__':
    print("{} + {} = {}".format(a, b, result))