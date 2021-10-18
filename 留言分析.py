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
        
