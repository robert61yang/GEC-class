import sys
lines = []
for line in sys.stdin.readlines():
    lines.append(line.strip())

lh = lines[0].split(',')
low = int(lh[0])
high = int(lh[1])

avoids = []
avo = lines[1].split(',')
for x in avo[:]:
    avoids.append(int(x))
#print(avoids)
output = []

def genNumList(low, high, avoids):
    outputs=""
    for num in range(low, high):
        match = False
        for avoid_num in avoids:
            if num % int(avoid_num) == 0:
                match = True
        if match == False:
                outputs += str(num) + ","
                output.append(num)
    return(outputs)

outString = genNumList(low,high, avoids)
print(outString[:len(outString)-1])
#print(output)

fd = lines[2].split(',')

#print(fd)
#print(outString.find('16'))
outp = ""
for x in fd[:]:
    try:
        y = output.index(int(x))
        y = int(y)+1
    except:
        y = 'N/A'
    outp += str(y) + ','

print(outp[:len(outp)-1])
