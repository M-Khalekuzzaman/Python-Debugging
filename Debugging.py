#How to work debugging in two perameters
def add(*numbers) :
    sum = 0
    for number in numbers :
        sum = sum + number
    return sum

print(add(10,20,30))