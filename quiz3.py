import sys

users = []
for line in sys.stdin.readlines():
    users.append(line.strip())


weight = users[0].split(' ')

weight[:] = [float(x) for x in weight]

q = len(weight)
score = []
students = []
c = 0
bonus = []


for user in users[1:]:  
    if 'BONUS' in user:
        y = int(user[5:])
        k = 0
        for x in users[1:c+1]:   
            data = x.split(',')
            ss = data[1+y].split('\\')
            #print(ss)
            cheat = False
            for p in data:
                if 'd' in p and int(p[1:]) == y:
                   cheat = True
            if ss[0] == ss[1] and bonus[k] == 0 and cheat == False:
                bonus[k] = 1
            k += 1
        #print(bonus)

    elif('X' in user):
        k = 0
        for x in users[1:c+1]:
            data = x.split(',')
            if(user[1:] in data[1]):
                score[k] = 0
            k += 1
    else:
        data = user.split(',')
        students.append(data[1])
        summ = []
        count = 0
        s = 0
        for x in data[2:2+q]:
            y = x.split('\\')
            summ.append(weight[count]*float(y[0])/float(y[1]))
            count += 1
        for x in data[2+q:]:
            if('d' in x):
                y = int(x[1:])
                summ[y-1] = 0
        score.append(sum(summ))
        c += 1
        bonus.append(int(0))
    

#print(score)

p = 0
for x in students:
    if bonus[p] == 0:
        s = round(score[p] * 100, 2)
    else:
        s = round(score[p] * 120, 2)
    print(x + ',' + "%.2f" %s)
    p += 1
