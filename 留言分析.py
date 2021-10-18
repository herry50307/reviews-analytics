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


new = []

for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有",len(new),"筆資料留言長度小於100")
print(new[0]) #把第一筆留言長度小於100的資料印出來


good = [] #把留言有good的資料抓出來
for d in data:
    if "good" in d:
        good.append(d)
print("一共有", len(good),"筆資料提到good")
