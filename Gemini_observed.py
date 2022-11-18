#!/usr/bin/env python

import sys,os
import re 
from mechanize import Browser
import requests
import numpy as np

import requests
from bs4 import BeautifulSoup
import urllib2


partner=sys.argv[1] #
semester=sys.argv[2] #2017A


#f=open('test.txt','w')
output_tmp='GS_'+partner+'_'+semester+'_tmp.txt'
f=open(output_tmp,'w')

#soup = BeautifulSoup(urllib2.urlopen('https://www.gemini.edu/sciops/schedules/schedQueue_GS_2017A.html',"lxml").read())
soup = BeautifulSoup(urllib2.urlopen('https://www.gemini.edu/sciops/schedules/schedQueue_GS_'+semester+'.html',"lxml").read())
arr=[]
#soup = BeautifulSoup(page.content)
for tr in soup.select("tr"):
    for td in tr.select("td"):
        lista=td.text.encode('utf-8')
        f.write(str(lista)+'\n')
        #a=td.text

f.close()

        #f = open('test.txt','r')
#lines = f.readlines()
#for line in f:
#    str2=line.replace('\n','')
#    print str2
#    #la.append(str2)

#print la

with open(output_tmp) as fin, open('newtest.txt', 'w') as fout:
#with open(output_tmp) as fin, open(, 'w') as fout:
    next(fin)
    next(fin)
    next(fin)
    next(fin)
    next(fin)
    next(fin)
    next(fin)
    next(fin)
    next(fin)
    for line in fin:
        if line.startswith('Title:'): 
            print(line,"aca2")
            fout.write(line)
        if (line.startswith("GS Scientific Ranking") or line.startswith("Ref #") or line.startswith("PI") or line.startswith("Partner") or line.startswith("Title") or line.startswith("Instrument") or line.startswith("Hoursallocated") or line.startswith("Hours") or line.startswith("GS Scientific Ranking Band 2") or  line.startswith("allocated")):
            #print(line,"here")
            continue
        

            #fout.write(line)
        if (line.startswith("GS Scientific Ranking") or line.startswith("Ref #") or line.startswith("PI") or line.startswith("Partner") or line.startswith("Title") or line.startswith("Instrument") or line.startswith("Hoursallocated") or line.startswith("Hours") or line.startswith("GS Scientific Ranking Band 2") or  line.startswith("allocated")):
            salto=True
            print(line,"here2")
            continue
        if line.startswith("Title:"): 
            print(line,"aca1")
            fout.write(line)    
        else:
            fout.write(line)     
#        elif "GS Scientific Ranking" not in line:
#            fout.write(line)    
#        elif "Ref #"  not in line:
#            fout.write(line)    
#        elif "PI" not in line:
#            fout.write(line)    
#        elif "Partner" not in line:
#            fout.write(line)    
#        elif "Title" not in line:
#            fout.write(line)    
#        elif "Instrument" not in line:
#            fout.write(line)    
#        elif "Hoursallocated" not in line:
#            fout.write(line)    
#        elif "Hours" not in line:
#            fout.write(line)    
#        elif "GS Scientific Ranking Band 2" not in line:
#            fout.write(line)    
#        elif "allocated" not in line:
#            fout.write(line)    

                
fout.close()
arr=[]
fp=open('newtest.txt','r')
for linea in fp:
    arr.append(linea)

arr2=np.array(arr)
print len(arr2)
b=[]
for i in range(0,int(len(arr2)),14):
    b.append(arr2[i:i+14])#,str("here\n")     

fp.close()
#f.write(str(lista)+'\n')
output='GS_'+partner+'_'+semester+'.txt'
f_out=open(output,'w')
#f_out.close()
#f_out=open(output,'a+')

b_arr=np.array(b)    
for j in range(len(b_arr)):
    N,PI,PAIS,TITLE,INST,hr,exe,d,w,COMPLE,DATE,z,comp_status,porcent=b_arr[j][0].splitlines(),(b_arr[j][1].splitlines()),(b_arr[j][2].splitlines()),(b_arr[j][3].splitlines()),b_arr[j][4].splitlines(),b_arr[j][5].splitlines(),b_arr[j][6].splitlines(),b_arr[j][7].splitlines(),b_arr[j][8].splitlines(),b_arr[j][9].splitlines(),b_arr[j][10].splitlines(),b_arr[j][11].splitlines(),b_arr[j][12].splitlines(),b_arr[j][13].splitlines()
    
    #print N,PI,PAIS,TITLE,INST,hr,exe,d,w,COMPLE,DATE,z,comp_status,porcent,j
    #print(TITLE)
    print(str(porcent[0])[:-1],str(hr[0]),"here",j,N)
    #print(PI[0])
    TOT_OBS=((float(str(porcent[0][:-1]))/100)*float(hr[0]))
    #rint TOT_OBS,PAIS
    if "CL" in str(PAIS[0]):
        #print N[0],PI[0],PAIS[0],TITLE[0],INST[0],hr[0],exe[0],d[0],w[0],COMPLE[0],DATE[0],z[0],comp_status[0],porcent[0]

        #todo=[N[0],PI[0],PAIS[0],str(TITLE[0]),INST[0],hr[0],exe[0],COMPLE[0],DATE[0],z[0],comp_status[0],porcent[0]]#,TOT_OBS]
        #print N[0],PI[0],PAIS[0],TITLE[0],INST[0],hr[0],exe[0],COMPLE[0],DATE[0],z[0],comp_status[0],porcent[0],TOT_OBS

        f_out.write(str(N[0])+','+str(PI[0])+','+str(PAIS[0])+','+str(TITLE[0])+','+str(INST[0])+','+str(hr[0])+','+str(exe[0])+','+str(COMPLE[0])+','+str(DATE[0])+','+str(z[0])+','+str(comp_status[0])+','+str(porcent[0])+','+str(TOT_OBS)+'\n')
        #f_out.write(str(N[0])+','+str(PI[0])+','+str(PAIS[0])+','+str(TITLE[0])+','+str(INST[0])+','+str(hr[0])+','+str(exe[0])+','+str(COMPLE[0])+','+str(DATE[0])+','+str(z[0])+','+str(comp_status[0])+','+str(porcent[0])+'\n')
        
    else:
        nada=1
#    #end
    

f_out.close()

