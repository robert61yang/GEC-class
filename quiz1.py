import sys
lines = []
for line in sys.stdin.readlines():
    lines.append(line.strip())

outString = ''

data = lines[0].split(',')
outString += data[2]

for x in range(int(data[0])):
    outString += data[1]
    outString += data[2]


print(outString)