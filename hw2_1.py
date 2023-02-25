import sys

words = []
for line in sys.stdin.readlines():
    words.append(line.strip())

e1 = float(words[0])
e2 = float(words[1])
e3 = int(words[2])
out1 = round(e1 * e2,1)
e4 = str(words[3])
out2 = e3 * e4
print(str(out1)+out2)