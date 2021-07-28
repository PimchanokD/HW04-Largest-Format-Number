# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:52:31 2021

@author: Pimchanok Duang-In 640631125
"""

def largest_number(value):
    listA = []
    n = len(str(value)) + 1
    for i in value:
        a = str(i) * n
        listA.append((a[:n:], i))
    listA.sort(reverse=True)
    
    answer = ''
    for i in listA:
        answer = answer + str(i[1])
    return answer

number = [10,1]
print('The largest formed number is' , largest_number(number))
