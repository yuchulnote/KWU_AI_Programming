#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pprint

Baseball = []

with open('hw2.csv', 'r') as csv_file:
    for line in csv_file:
        data = line.strip().split(',')
        Baseball.append(data)
        for d in data:
            print(d, end='\t')

stat_list = Baseball[0]
stat_tuple = tuple(stat_list)


# In[2]:


def Player():
    x = input("선수이름을 입력해주세요 : ")
    for info in Baseball:
        if info[0] == x:
            print(info[1:])
            break
    else:
        print("없는 선수입니다")


# In[3]:


def Val():
    x = input("선수이름을 입력해주세요 : ")
    
    for info in Baseball:
        if info[0] == x:
            y = stat_tuple.index(input("보고싶은 통계를 입력하세요 : "))
            print(info[y])


# In[4]:


Matrix = np.array(Baseball)
Matrix.shape


# In[5]:


def sort():
        x = stat_tuple.index(input("통계를 선택하세요 : "))

        Name = Matrix[1:,0]
        Character = Matrix[1:,x]
        
        Name_list = Name.tolist()
        Char_list = Character.tolist()
        Char_list = list(map(int, Char_list))
        
        Dic = dict(zip(Name_list, Char_list))
        sorted_Dic = sorted(Dic.items(), key=lambda item: item[1], reverse=True)
        pprint.pprint(sorted_Dic)


# In[6]:


#TEST
Player()
Val()
sort()

