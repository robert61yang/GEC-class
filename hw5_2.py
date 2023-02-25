import sys

input_list = []
for line in sys.stdin.readlines():
    input_list.append(line.strip())

def count_al(i_str, al_dict={}):
    for al in i_str:
        if al not in al_dict.keys():
            al_dict[al] = 1
        else:
            al_dict[al] = al_dict[al] + 1
    return al_dict

def sortDic(inDic):
    sortList=[]
    sortList = sorted(inDic.items(),key=lambda pair: pair[1],reverse=True)
    return(sortList)


def dec(i_str,L = []):
    k = len(L)
    count = 0
    outS=''
    for x in i_str: 
        if count == k-2:
            if x == '0':
                outS += L[k-1][0]
                count = 0
            elif x == '1':
                outS += L[k-2][0]
                count = 0
        elif x == '0':
            count += 1
        elif x == '1':
            outS += L[count][0]
            count = 0
    print(outS)

al_dict = {}

al_dict = count_al(input_list[0].lower(), al_dict)
sortL = sortDic(al_dict)



dec(input_list[1],sortL)