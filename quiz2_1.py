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

songs = input_list[0].split(',')

if len(songs) <= 3:
    print(input_list[0])
else:
    for x in songs:
        if x in thisDist:
            thisDist[x] += 1
        else:
            thisDist[x] = 1
    for x in thisDist:
        if thisDist[x] > f_max:
            if x != f:
                t_max = s_max
                t = s
                s_max = f_max
                s = f
            f = x
            f_max = thisDist[x]
        elif thisDist[x] > s_max:
            if x != s:
                t_max = s_max
                t = s
            s = x
            s_max = thisDist[x]
        elif thisDist[x] > t_max:
            t = x
            t_max = thisDist[x]
    print(f+','+s+','+t)
        

