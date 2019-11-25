# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:34:41 2019

@author: lenovo
"""

import networkx as nx
import matplotlib.pyplot as plt
import fiona
import csv

"""
G = nx.Graph()#无向图

with fiona.open('C:/Users/lenovo/Desktop/shp/test/splitLineAtPoint.shp','r') as src:
    for f in src.items():
        
        print("startId:", f[1]['properties']['startId']);
        print("endId:", f[1]['properties']['endId']);
        print("distance:", f[1]['properties']['distance']);
        
        G.add_weighted_edges_from([(f[1]['properties']['startId'], f[1]['properties']['endId'], f[1]['properties']['distance'])])
    src.close()

nx.draw(G, with_labels=True)
plt.show()

L = nx.all_pairs_dijkstra_path_length(G)
#L = nx.all_pairs_shortest_path_length(G)
#path = nx.all_pairs_shortest_path(G)
#print(next(path))
print(next(L))
"""

IdDict={}

with fiona.open('F:/myStudy/graduateWork/稀疏矩阵/北京/bjMap6Proj.shp','r') as src, open('F:/myStudy/graduateWork/稀疏矩阵/北京/bjMap6Dir.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id","onway","distance","start_x","start_y","end_x","end_y","startId","endId",
                     "wealthy","safety","lively","beautiful","boring","depression",
                     "startNodeid","endNodeid",
                     "100_wealthy","100_safety","100_lively","100_beautiful","100_boring","100_depression"])
    index=1
    for f in src.items(): 
        if f[1]['properties']['startId'] not in IdDict.keys():
            IdDict[f[1]['properties']['startId']]=index
            index+=1
        if f[1]['properties']['endId'] not in IdDict.keys():
            IdDict[f[1]['properties']['endId']]=index
            index+=1
            
    for f in src.items(): 
        """
        print("id:", f[1]['properties']['id'])
        print("oneway:", f[1]['properties']['oneway'])
        print("distance:", f[1]['properties']['distance'])
        print("startId:", f[1]['properties']['startId'])
        print("endId:", f[1]['properties']['endId'])
        print("wealthy:", f[1]['properties']['wealthy'])
        print("safety:", f[1]['properties']['safety'])
        print("lively:", f[1]['properties']['lively'])
        print("beautiful:", f[1]['properties']['beautiful'])
        print("boring:", f[1]['properties']['boring'])
        print("depression:", f[1]['properties']['depression'])
        """         
        arr=[]
        """
        arr.append(f[1]['properties']['id'])
        arr.append(f[1]['properties']['oneway'])
        arr.append(f[1]['properties']['distance'])
        arr.append(f[1]['properties']['start_x'])
        arr.append(f[1]['properties']['start_y'])
        arr.append(f[1]['properties']['end_x'])
        arr.append(f[1]['properties']['end_y'])
        arr.append(f[1]['properties']['startId'])
        arr.append(f[1]['properties']['endId'])
        arr.append(f[1]['properties']['wealthy'])
        arr.append(f[1]['properties']['safety'])
        arr.append(f[1]['properties']['lively'])
        arr.append(f[1]['properties']['beautiful'])
        arr.append(f[1]['properties']['boring'])
        arr.append(f[1]['properties']['depression'])   
        arr.append(IdDict[f[1]['properties']['startId']]) 
        arr.append(IdDict[f[1]['properties']['endId']])     
        """
        #oneway代表道路方向，"B"代表双向，"T"代表仅反向，  "F"代表仅正向
        if f[1]['properties']['oneway']=="B": 
            arr.clear()
            arr.append(f[1]['properties']['id'])
            arr.append(f[1]['properties']['oneway'])
            arr.append(f[1]['properties']['distance'])
            arr.append(f[1]['properties']['start_x'])
            arr.append(f[1]['properties']['start_y'])
            arr.append(f[1]['properties']['end_x'])
            arr.append(f[1]['properties']['end_y'])
            arr.append(f[1]['properties']['startId'])
            arr.append(f[1]['properties']['endId'])        
            arr.append(f[1]['properties']['wealthy'])
            arr.append(f[1]['properties']['safety'])
            arr.append(f[1]['properties']['lively'])
            arr.append(f[1]['properties']['beautiful'])
            arr.append(f[1]['properties']['boring'])
            arr.append(f[1]['properties']['depression'])        
            arr.append(IdDict[f[1]['properties']['startId']]) 
            arr.append(IdDict[f[1]['properties']['endId']])
            arr.append(100-f[1]['properties']['wealthy'])
            arr.append(100-f[1]['properties']['safety'])
            arr.append(100-f[1]['properties']['lively'])
            arr.append(100-f[1]['properties']['beautiful'])
            arr.append(100-f[1]['properties']['boring'])
            arr.append(100-f[1]['properties']['depression'])
            writer.writerow(arr)
            
            arr.clear()
            arr.append(f[1]['properties']['id'])
            arr.append(f[1]['properties']['oneway'])
            arr.append(f[1]['properties']['distance'])
            arr.append(f[1]['properties']['end_x'])
            arr.append(f[1]['properties']['end_y'])
            arr.append(f[1]['properties']['start_x'])
            arr.append(f[1]['properties']['start_y'])
            arr.append(f[1]['properties']['endId']) 
            arr.append(f[1]['properties']['startId'])   
            arr.append(f[1]['properties']['wealthy'])
            arr.append(f[1]['properties']['safety'])
            arr.append(f[1]['properties']['lively'])
            arr.append(f[1]['properties']['beautiful'])
            arr.append(f[1]['properties']['boring'])
            arr.append(f[1]['properties']['depression']) 
            arr.append(IdDict[f[1]['properties']['endId']])
            arr.append(IdDict[f[1]['properties']['startId']])
            arr.append(100-f[1]['properties']['wealthy'])
            arr.append(100-f[1]['properties']['safety'])
            arr.append(100-f[1]['properties']['lively'])
            arr.append(100-f[1]['properties']['beautiful'])
            arr.append(100-f[1]['properties']['boring'])
            arr.append(100-f[1]['properties']['depression'])
            writer.writerow(arr)  
        if f[1]['properties']['oneway']=="F":
            arr.clear()
            arr.append(f[1]['properties']['id'])
            arr.append(f[1]['properties']['oneway'])
            arr.append(f[1]['properties']['distance'])
            arr.append(f[1]['properties']['start_x'])
            arr.append(f[1]['properties']['start_y'])
            arr.append(f[1]['properties']['end_x'])
            arr.append(f[1]['properties']['end_y'])
            arr.append(f[1]['properties']['startId'])
            arr.append(f[1]['properties']['endId'])        
            arr.append(f[1]['properties']['wealthy'])
            arr.append(f[1]['properties']['safety'])
            arr.append(f[1]['properties']['lively'])
            arr.append(f[1]['properties']['beautiful'])
            arr.append(f[1]['properties']['boring'])
            arr.append(f[1]['properties']['depression'])        
            arr.append(IdDict[f[1]['properties']['startId']]) 
            arr.append(IdDict[f[1]['properties']['endId']])
            arr.append(100-f[1]['properties']['wealthy'])
            arr.append(100-f[1]['properties']['safety'])
            arr.append(100-f[1]['properties']['lively'])
            arr.append(100-f[1]['properties']['beautiful'])
            arr.append(100-f[1]['properties']['boring'])
            arr.append(100-f[1]['properties']['depression'])
            writer.writerow(arr)
        if f[1]['properties']['oneway']=="T":
            arr.clear()
            arr.append(f[1]['properties']['id'])
            arr.append(f[1]['properties']['oneway'])
            arr.append(f[1]['properties']['distance'])
            arr.append(f[1]['properties']['end_x'])
            arr.append(f[1]['properties']['end_y'])
            arr.append(f[1]['properties']['start_x'])
            arr.append(f[1]['properties']['start_y'])
            arr.append(f[1]['properties']['endId']) 
            arr.append(f[1]['properties']['startId'])   
            arr.append(f[1]['properties']['wealthy'])
            arr.append(f[1]['properties']['safety'])
            arr.append(f[1]['properties']['lively'])
            arr.append(f[1]['properties']['beautiful'])
            arr.append(f[1]['properties']['boring'])
            arr.append(f[1]['properties']['depression']) 
            arr.append(IdDict[f[1]['properties']['endId']])
            arr.append(IdDict[f[1]['properties']['startId']])
            arr.append(100-f[1]['properties']['wealthy'])
            arr.append(100-f[1]['properties']['safety'])
            arr.append(100-f[1]['properties']['lively'])
            arr.append(100-f[1]['properties']['beautiful'])
            arr.append(100-f[1]['properties']['boring'])
            arr.append(100-f[1]['properties']['depression'])
            writer.writerow(arr)
    src.close()
    csvfile.close()
