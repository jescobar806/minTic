
first = 0
second = 1
print (first)
print (second)
for i in range (0,51):
    number = first + second
    first = second
    second = number
    print (number)
