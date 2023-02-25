import sys

input_list = []
for line in sys.stdin.readlines():
    input_list.append(line.strip())

#print(input_list)

thisDist = {
}

f_max = 0
s_max = 0
t_max = 0

f = ''
s = ''
t = ''


for x in input_list[:]:
    x = x.split(',') 
    if x[0] in thisDist:
        thisDist[x[0]] += float(x[1])
    else:
        thisDist[x[0]] = 0 
        thisDist[x[0]] += float(x[1])
    if thisDist[x[0]] >= f_max:
        if x[0] != f:
            t_max = s_max
            t = s
            s_max = f_max
            s = f
        f = x[0]
        f_max = thisDist[x[0]]
    elif thisDist[x[0]] >= s_max:
        if x[0] != s:
            t_max = s_max
            t = s
        s = x[0]
        s_max = thisDist[x[0]]
    elif thisDist[x[0]] >= t_max:
        t = x[0]
        t_max = thisDist[x[0]]

print(f + ',' +  str(f_max))
print(s + ',' +  str(s_max))
print(t + ',' +  str(t_max))



