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

for user in users[1:]:
    if('X' in user):
        for x in users[1:c]:
            data = x.split(',')
            if(user[1:] in data[1]):
               score[int(x[0])-1] = 0
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

p = 0
for x in students:
    s = round(score[p] * 100, 2)
    print(x + ',' + "%.2f" %s)
    p += 1