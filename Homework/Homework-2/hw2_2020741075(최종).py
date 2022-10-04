import numpy as np
import pprint

Baseball = []

with open('hw2.csv', 'r') as csv_file:
    for line in csv_file:
        data = line.strip().split(',')
        for d in data:
            print(d, end='\t')
        Baseball.append(data)

status = Baseball[0]

def name():
    name = input("선수명을 입력하시오 : ")
    for i in Baseball:
        if i[0] == name:
            print(i[1:])
            break
    else:
        print("error")
        
def stat():
    name = input("선수명을 입력하시오 : ")
    stat = input("보고싶은 통계를 입력하시오 : ")
    
    x = status.index(stat)
    
    for i in Baseball:
        if i[0] == name:
            print(i[x])
            
Matrix = np.array(Baseball)

def sort():
    x = status.index(input("보고싶은 통계를 입력하시오 : "))
    name = Matrix[1:,0]
    stat = Matrix[1:,x]
    
    name_list = name.tolist()
    stat_list = stat.tolist()
    stat_list = list(map(int, stat_list))
    
    Dic = dict(zip(name_list, stat_list))
    
    sorted_dic = sorted(Dic.items(), key = lambda x:x[1], reverse=True)
    pprint.pprint(sorted_dic)
    
