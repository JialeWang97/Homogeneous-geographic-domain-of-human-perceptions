# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 00:17:56 2019

@author: lenovo
"""
import csv

myDict={}
#读取csv，将点id和经纬度对应上 9-14为wealthy、safety、lively、beautiful、boring、depression的分数
def readcsvannid():   
    with open('F:/myStudy/graduateWork/稀疏矩阵/北京/bjMap6Dir.csv','r') as csvfile:
        reader = csv.reader(csvfile)      
        next(reader)  
        for aline in reader:
            arr=[]
            arr.clear()           
            arr.append(aline[3])
            arr.append(aline[4])                   
            myDict[aline[15]] = arr
            arr.clear()  
            arr.append(aline[5])
            arr.append(aline[6])
            myDict[aline[16]] = arr
        #print(myDict)              
        csvfile.close()
    
        
def readtxtandwritescv():      
    with open('F:/myStudy/graduateWork/稀疏矩阵/北京/output/bjbeutifulDirTree.txt', 'r') as f, open('F:/myStudy/graduateWork/稀疏矩阵/北京/outputcsv/bjbeutifulDirTreeTopLevel.csv','w',newline='') as csvfile:     
        writer = csv.writer(csvfile)
        writer.writerow(["lon","lat","toplevel"])
        for line in f:
            arr=[]
            arr.clear()
            ls=line.split(' ')
            levelList=ls[0].split(':')
            level=levelList[0]
            pntid=ls[3].replace('\n', '')
            lon=myDict[str(pntid)][0]
            lat=myDict[str(pntid)][1]
            arr.append(lon)
            arr.append(lat)
            arr.append(level)
            writer.writerow(arr)
        csvfile.close()

readcsvannid()
readtxtandwritescv()     