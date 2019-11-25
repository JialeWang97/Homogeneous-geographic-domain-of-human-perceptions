# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:33:05 2019

@author: lenovo
"""
import fiona

#统计各类poi的数目
poipath=['poi1_','poi2_','poi3_','poi4_']

mydict={}
mydict['FS']=0#finacial service
mydict['ME']=0#medical and education
mydict['ENT']=0#entertainment
mydict['GOV']=0#goverment
mydict['RC']=0#residence communities
mydict['LS']=0#life service
mydict['OBS']=0#office building space
mydict['OTH']=0#other

count=0
for p in poipath:
    with fiona.open('F:/myStudy/graduateWork/稀疏矩阵/北京/poi/'+p+'.shp', mode='r') as src:
        for f in src.items():
            count+=1
            if count%5000==0:
                print(count)
            if f[1]['properties']['typecode'] is None:
                mydict['OTH']+=1
                continue
            if f[1]['properties']['typecode']=='':
                mydict['OTH']+=1
                continue
            if str(f[1]['properties']['typecode']).find('|')!=-1:
                print(str(f[1]['properties']['typecode']))
                arr=f[1]['properties']['typecode'].split('|')
                for codestr in arr:
                    code=int(codestr)
                    if code>=160000 and code<=160600:
                        mydict['FS']+=1
                    if (code>=90000 and code<=90702) or (code>=140000 and code<=141500):
                        mydict['ME']+=1
                    if (code>=80000 and code<=80603) or (code>=100000 and code<=110209):
                        mydict['ENT']+=1
                    if code>=130000 and code<=130703:
                        mydict['GOV']+=1
                    if code>=120000 and code<=120304:
                        mydict['RC']+=1
                    if code>=50000 and code<=72001:
                        mydict['LS']+=1
                    if code>=170000 and code<=170408:
                        mydict['OBS']+=1
                    if code<50000 or code>=180000 or (code>=150000 and code<160000):
                        mydict['OTH']+=1
                continue
            
            typecode=int(f[1]['properties']['typecode'])
            
            if typecode>=160000 and typecode<=160600:
                mydict['FS']+=1
                continue
            if (typecode>=90000 and typecode<=90702) or (typecode>=140000 and typecode<=141500):
                mydict['ME']+=1
                continue
            if (typecode>=80000 and typecode<=80603) or (typecode>=100000 and typecode<=110209):
                mydict['ENT']+=1
                continue
            if typecode>=130000 and typecode<=130703:
                mydict['GOV']+=1
                continue
            if typecode>=120000 and typecode<=120304:
                mydict['RC']+=1
                continue
            if typecode>=50000 and typecode<=72001:
                mydict['LS']+=1
                continue
            if typecode>=170000 and typecode<=170408:
                mydict['OBS']+=1
                continue
            mydict['OTH']+=1
        src.close()
print(mydict)
print(count)
            
                
        
