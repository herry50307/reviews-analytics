# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:05:29 2021

@author: DSC Handsome
"""

data =[]
count = 0
with open("reviews.txt","r") as f:
    for line in f:
        data.append(line)
        count+=1
        if count % 10000==0:
            print(len(data))
print("總共有",len(data),"筆資料")
        
sumlen = 0
for d in data: #每一筆字串取出放到d
    sumlen = sumlen+len(d) #每一筆字串總和相加
    """
    print("總共留言長度",sumlen)
    """
    
print("平均留言長度是: ",sumlen/len(data))
