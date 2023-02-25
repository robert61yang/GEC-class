import sys

input_list = []
for line in sys.stdin.readlines():
    input_list.append(line.strip())


songs = input_list[2].split(',')
songs[0] = songs[0].replace('{','')
l = len(songs)
songs[l-1] = songs[l-1].replace('}','')

folders = input_list[1].split(',')
folders[0] = folders[0].replace('[','')
ll = len(folders)
folders[ll-1] = folders[ll-1].replace(']','')


if input_list[0] == 'Division':
    M = 0
    for x in songs:
        M += len(x)
    M += 1
    outS = '{'
    for x in songs:
        loca = str(int(x) % M)
        l = len(loca)
        lo = int(loca[l-2:])
        outS += x
        outS += ':'
        outS += folders[lo].replace(' ','')
        outS += ','
    s = len(outS)
    print(outS[:s-1]+'}')
elif input_list[0] == 'Folding':
    M = 0
    for x in songs:
        M += len(x)
    M += 1
    outS ='{'
    for x in songs:
        part = int(len(x) / 3)
        a = int(x[:part])
        b = x[part:len(x)-part]
        c = int(x[len(x)-part:])
        b = int(b[::-1])
        loca = str((a+b+c) % M)
        l = len(loca)
        lo = int(loca[l-2:])
        outS += x
        outS += ':'
        outS += folders[lo].replace(' ','')
        outS += ','
    s = len(outS)
    print(outS[:s-1]+'}')
