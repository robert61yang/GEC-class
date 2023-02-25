import sys

input_list = []
for line in sys.stdin.readlines():
    input_list.append(line.strip())

n = int(input_list[0])
art =  []
out = []

for line in input_list[1:]:
    art += line.split(" ")

if n > len(art):
    n = len(art)


out.append(art[0])

for x in art[1:]:
    k = 0
    for y in out[:]:
        if len(x) > len(y):
            k += 1  
        elif len(x) == len(y):
            or_x = 0
            or_y = 0
            for p in x:
                or_x += ord(p)
            for p in y:
                or_y += ord(p)
            #print(x+" " + str(or_x)+" " + str(or_y)+" "+ y)
            if or_x > or_y:
                k+=1
            else:
                out.insert(k,x)
                break
            
        elif len(x) < len(y):    
            out.insert(k,x)
            break
    if k == len(out):
        out.append(x)

#print(out)

for x in range(n):
    print(out.pop())
