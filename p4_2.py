import sys
lines = []
for line in sys.stdin.readlines():
    lines.append(line.strip())

abcString = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

testString = ""
for x in lines[:]:
    testString += x 

testString = testString.replace(',','')

minn = -1
ans = ''

for x in testString[:]:
    ori = len(testString)
    testString = testString.replace(x,'')
    length = ori - len(testString)
    if minn == -1:
        minn = length
        ans = x
    elif length < minn and length != 0:
        minn = length
        ans = x
        
print(ans + ',' + str(minn))


'''
minn = -1
ans = ''

for x in abcString[:]:
    ori = len(testString)
    testString = testString.replace(x,'')
    length = ori - len(testString) 
    if minn == -1:
        minn = length
        ans = x
    elif length < minn and length != 0:
        minn = length
        ans = x

print(ans + ',' + str(minn))
'''