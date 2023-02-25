import sys

input_list = []
for line in sys.stdin.readlines():
    input_list.append(line.strip())

al_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def count_al(i_str, al_dict={}):
    for al in i_str:
        if al not in al_dict.keys() and  al != ' ':
            al_dict[al] = 1
        elif al != ' ':
            al_dict[al] = al_dict[al] + 1
    return al_dict

def sortDic(inDic):
    sortList=[]

    sortList = sorted(inDic.items(),key=lambda pair: pair[1],reverse=True)
    return(sortList)


def outDic(sortL=[]):
    o_dict = {}
    i = 0
    for x in sortL: 
       o_dict[x[0]] = al_list[i]
       i += 1
    return o_dict

al_dict = {}
out_dict = {}

for line in input_list:
    count_al(line, al_dict)

sortL = sortDic(al_dict)

out_dict = outDic(sortL)

#print(out_dict)

for line in input_list:
    outS =''
    for x in line:
        if x !=' ':
            outS += out_dict[x]
        else:
            outS += ' '
    print(outS)