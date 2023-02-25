import sys

users = []
for line in sys.stdin.readlines():
    users.append(line.strip())
for user in users:
    data = user.split(",")
    passed = data[1][2:3]
    score = round(float(int(data[2])/int(passed))*100,2)
    print(data[0]+","+ "%.2f" %score)