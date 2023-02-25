import sys

input_list = []
for line in sys.stdin.readlines():
    input_list.append(line.strip())

s = input_list[1]
names = input_list[0].split(s)
outS=""
print(names)

for name in names[:]:
    outS += s
    thisDist = {}
    for x in name:
        if x.lower() in thisDist:
            name = name.replace(x.lower(),"")
            name = name.replace(x.upper(),"")
        else:
            thisDist[x.lower()] = 1
    outS += name 

l = len(s)
print(outS[l:])