# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:36:38 2019

@author: lenovo
"""
import csv
import fiona
import math

#计算各社区的poi数目
#输出 社区标号 FS数目 ME数目 ENT数目 GOV数目 RC数目 LS数目 OBS数目 总数目 FS比例 ME比例 ENT比例 GOV比例 RC比例 LS比例 OBS比例 信息熵

count=0
category='depression'
ppath='F:/myStudy/graduateWork/稀疏矩阵/北京/poi分析/bj'+category+'修改后.csv'
patharr=['poi1_','poi2_','poi3_','poi4_']
cdict={}
for p in patharr:
    with fiona.open('F:/myStudy/graduateWork/稀疏矩阵/北京/outputcsv/allpoiidentify/bj'+ category + p + 'iden.shp', mode='r') as src:
        for f in src.items():
            if int(f[1]['properties']['thirdlevel'])!=0 and f[1]['properties']['thirdlevel'] not in cdict.keys():
                arr=[int(f[1]['properties']['thirdlevel']),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                cdict[f[1]['properties']['thirdlevel']]=arr
        src.close()
        
for p in patharr:
    with fiona.open('F:/myStudy/graduateWork/稀疏矩阵/北京/outputcsv/allpoiidentify/bj'+ category + p + 'iden.shp', mode='r') as src:        
        for f in src.items():
            count+=1
            if count%5000==0:
                print(count)
            if int(f[1]['properties']['thirdlevel'])==0:
                continue           
            
            if f[1]['properties']['typecode'] is None:                
                continue
            if f[1]['properties']['typecode']=='':
                continue
            if str(f[1]['properties']['typecode']).find('|')!=-1:
                arr=f[1]['properties']['typecode'].split('|')
                for codestr in arr:
                    code=int(codestr)
                    if code>=160000 and code<=160600:
                        cdict[f[1]['properties']['thirdlevel']][1]+=1
                        cdict[f[1]['properties']['thirdlevel']][8]+=1
                    if (code>=90000 and code<=90702) or (code>=140000 and code<=141500):
                        cdict[f[1]['properties']['thirdlevel']][2]+=1
                        cdict[f[1]['properties']['thirdlevel']][8]+=1
                    if (code>=80000 and code<=80603) or (code>=100000 and code<=110209):
                        cdict[f[1]['properties']['thirdlevel']][3]+=1
                        cdict[f[1]['properties']['thirdlevel']][8]+=1
                    if code>=130000 and code<=130703:
                        cdict[f[1]['properties']['thirdlevel']][4]+=1
                        cdict[f[1]['properties']['thirdlevel']][8]+=1
                    if code>=120000 and code<=120304:
                        cdict[f[1]['properties']['thirdlevel']][5]+=1
                        cdict[f[1]['properties']['thirdlevel']][8]+=1
                    if code>=50000 and code<=72001:
                        cdict[f[1]['properties']['thirdlevel']][6]+=1
                        cdict[f[1]['properties']['thirdlevel']][8]+=1
                    if code>=170000 and code<=170408:
                        cdict[f[1]['properties']['thirdlevel']][7]+=1
                        cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue
            
            typecode=int(f[1]['properties']['typecode'])           
            if typecode>=160000 and typecode<=160600:
                cdict[f[1]['properties']['thirdlevel']][1]+=1
                cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue
            if (typecode>=90000 and typecode<=90702) or (typecode>=140000 and typecode<=141500):
                cdict[f[1]['properties']['thirdlevel']][2]+=1
                cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue
            if (typecode>=80000 and typecode<=80603) or (typecode>=100000 and typecode<=110209):
                cdict[f[1]['properties']['thirdlevel']][3]+=1
                cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue
            if typecode>=130000 and typecode<=130703:
                cdict[f[1]['properties']['thirdlevel']][4]+=1
                cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue
            if typecode>=120000 and typecode<=120304:
                cdict[f[1]['properties']['thirdlevel']][5]+=1
                cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue
            if typecode>=50000 and typecode<=72001:
                cdict[f[1]['properties']['thirdlevel']][6]+=1
                cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue
            if typecode>=170000 and typecode<=170408:
                cdict[f[1]['properties']['thirdlevel']][7]+=1
                cdict[f[1]['properties']['thirdlevel']][8]+=1
                continue                    
        src.close()

for k in cdict.keys():
    if cdict[k][8]==0:
        continue
    cdict[k][9]=(cdict[k][1]/cdict[k][8])
    cdict[k][10]=(cdict[k][2]/cdict[k][8])
    cdict[k][11]=(cdict[k][3]/cdict[k][8])
    cdict[k][12]=(cdict[k][4]/cdict[k][8])
    cdict[k][13]=(cdict[k][5]/cdict[k][8])
    cdict[k][14]=(cdict[k][6]/cdict[k][8])
    cdict[k][15]=(cdict[k][7]/cdict[k][8])
    
    for i in range(9,16):
        if cdict[k][i]==0:
            continue
        cdict[k][16]-=(cdict[k][i]*math.log(cdict[k][i]))

#FS比例 ME比例 ENT比例 GOV比例 RC比例 LS比例 OBS比例    
for k in cdict.keys():
    cdict[k][17]=(cdict[k][9]/0.017874307)
    cdict[k][18]=(cdict[k][10]/0.06084236)
    cdict[k][19]=(cdict[k][11]/0.036925418)
    cdict[k][20]=(cdict[k][12]/0.027694301)
    cdict[k][21]=(cdict[k][13]/0.025434724)
    cdict[k][22]=(cdict[k][14]/0.40931014)
    cdict[k][23]=(cdict[k][15]/0.122306839)    
   
   
with open(ppath,'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['level','FSnum','MEnum','ENTnum','GOVnum','RCnum','LSnum','OBSnum','Sum','FSpro','MEpro','ENTpro','GOVpro','RCpro','LSpro','OBSpro','Entropy','E_FSpro','E_MEpro','E_ENTpro','E_GOVpro','E_RCpro','E_LSpro','E_OBSpro'])
    
    for k in cdict.keys():
        writer.writerow(cdict[k])
    csvfile.close()
    
















