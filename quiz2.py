import sys

number_list = []
for line in sys.stdin.readlines():
    number_list.append(line.strip())
numbers = number_list[0].split(',')


#print(numbers)
iter = 0



for number in numbers[0:]:
    if(number == 'i1'):
        iter = 1
        numbers.remove(number)
    elif(number == 'i2'):
        iter = 2
        numbers.remove(number)

numbers[:] = [int(x) for x in numbers]

if(iter == 1):
    print(max(numbers))
elif(iter == 2):
    print(min(numbers))
   