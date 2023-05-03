try:
    print(1)
except ZeroDivisionError:
    print(2)
else:#if no error occures
    print(3)
finally:
    print("Final Block")

try:
    print(6)
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)
finally:
    print("Final Block")