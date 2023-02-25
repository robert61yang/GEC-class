import sys

input_list = []
for line in sys.stdin.readlines():
    input_list.append(line.strip())


albums = input_list[0].split(',')
al_dict = {}
ti_dict = {}


for x in albums:
    c = 0
    for y in x[::-1]:
        if y == ' ' :
            break
        else:
            c += 1
    al_dict[x[:len(x)-c-1]] = x[len(x)-c:].replace('minutes','')
   
for x in input_list[1:]:
    song = ''
    for y in al_dict:
        if y in x:
            song = y
            break
    x = x.replace(song,'')
    q = x.split(' ')
    
    time = int(int(al_dict[song]) * 180 / 10)
    song_long = int(al_dict[song]) * 60

    if q[0] in q[2]:
        start = q[1].split(':')
        end = q[3].split(':')
        if 'PM' in q[2]:
            if start[0] == '12':
                start[0] = '0'
            start[0] = str(int(start[0]) + 12)
        if 'PM' in q[4]:
            if end[0] == '12':
                end[0] = '0'
            end[0] = str(int(end[0]) + 12)
        start_t = int(start[0])*3600 + int(start[1]) * 60 + int(start[2])
        end_t = int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])
        dur_t = end_t - start_t
        count = 0
        if dur_t >= time:
            if dur_t >= 14400:
                count = 1
            else:
                count += int(dur_t/song_long)
                if dur_t % song_long >= time:
                    count += 1
            if song not in ti_dict.keys() and count != 0:
                ti_dict[song] = count
            elif count != 0:
                ti_dict[song] += count
    else:
        if 'AM' in q[4] and 'PM' in q[2]:
            start = q[1].split(':')
            end = q[3].split(':')
            start[0] = str(int(start[0]) + 12)
            start_t = int(start[0])*3600 + int(start[1]) * 60 + int(start[2])
            end_t = int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])
            dur_t = 24 * 3600 - start_t + end_t
            count = 0
            if dur_t >= time:
                if dur_t >= 14400:
                    count = 1
                else:
                    count += int(dur_t/song_long)
                    if dur_t % song_long >= time:
                        count += 1
                if song not in ti_dict.keys() and count != 0:
                    ti_dict[song] = count
                elif count != 0:
                    ti_dict[song] += count
        else:
            count = 1
            if song not in ti_dict.keys():
                    ti_dict[song] = count
            else:
                ti_dict[song] += count

f_max = 0
s_max = 0
t_max = 0

f = ''
s = ''
t = ''

if len(ti_dict.keys()) >= 3:
    for x in ti_dict:
            if ti_dict[x] > f_max:
                if x != f:
                    t_max = s_max
                    t = s
                    s_max = f_max
                    s = f
                f = x
                f_max = ti_dict[x]
            elif ti_dict[x] > s_max:
                if x != s:
                    t_max = s_max
                    t = s
                s = x
                s_max = ti_dict[x]
            elif ti_dict[x] > t_max:
                t = x
                t_max = ti_dict[x]
    print(f+','+s+','+t)
else:
    if len(ti_dict.keys()) == 1:
        for x in ti_dict:
            print(x)
    else:
        big = 0
        bigx = ''
        sec = 0
        secx =''
        for x in ti_dict:
            if ti_dict[x] > big:
                sec = big
                secx = bigx
                big = ti_dict[x]
                bigx = x
            elif ti_dict[x] > sec:
                sec= ti_dict[x]
                secx = x
    print(bigx+','+secx)

