import sys

number_list = []
for line in sys.stdin.readlines():
    number_list.append(line.strip())
numbers = number_list[0].split(',')

iter = 0
range = len(numbers)
front = True
dele = False

for number in numbers[0:]:
    if(number == 'i1'):
        iter = 1
        numbers.remove(number)
    elif(number == 'i2'):
        iter = 2
        numbers.remove(number)
    elif 'f' in number:
        range = int(number[1:])
        front = True
        numbers.remove(number)
        dele = True
    elif 'b' in number:
        range = int(number[1:])
        front = False
        numbers.remove(number)  
        dele = True
    #int(number)

numbers[:] = [int(x) for x in numbers]

if(iter == 1):
    if(dele == False):
        print(max(numbers))
    elif(front == True):
        print(max(numbers[:range]))
    elif(front == False):
        print(max(numbers[len(numbers)-range:]))
elif(iter == 2):
    if(dele == False):
        print(min(numbers))
    elif(front == True):
        print(min(numbers[:range]))
    elif(front == False):
        print(min(numbers[len(numbers)-range :]))
