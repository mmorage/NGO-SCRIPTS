#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os,sys,string
import numpy as np
from lxml.etree import parse as lparse

#read each xml file into an array
files= [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f.endswith(('.xml')):
        #print f
        #change the output .txt
        #file_out=f[:-3]+'_delme_.txt' 
        #print file_out


        inti=[]
        address=[]
         
        ltree= lparse(f)
        tree = ET.parse(f) #setup ETread
        root = tree.getroot() #define root 

        #get PI name
        # .encode('utf-8') used to avoid accents and other characters
        for pi in root.iter('pi'):
            pilastname= pi.find('lastName').text.encode('utf-8')
            piname=pi.find('firstName').text.encode('utf-8')
            email=pi.find('email').text


        for pi in root.iter('pi'):
            #time per partner
            address.append(pi.find('address'))
            for address in pi.iter('address'): 
                for institution in address.iter('institution'):
                    inti=institution.text
                    #print(institution.text)
                    #print(address.institution.text)
                    #inti=pi.address.find('institution').text
                    #inti.append(pi.address.find('institution').text)
                    #tiempo_min.append(request.find('minTime').text)
                    #for response in ngo.iter('response'):
                    #    for receipt in response.iter('receipt'):



        for proposal in root.iter('proposal'):
            Title=proposal.find('title').text

        #print(institution)
        #print(inti)
        #exit()
        
        #arrays
        partner=[]
        tiempo_req=[]
        tiempo_min=[]
        
        tiempo_req3=[]
        tiempo_min3=[]
        
        for proposalClass in root.iter('proposalClass'):
            for queue in proposalClass.iter('queue'): 
                #print queue.tag, queue.attrib
                Too= queue.get('tooOption')  #asking if it is a ToO
                
                for ngo in queue.iter('ngo'):
                    #time per partner
                    partner.append(ngo.find('partner').text)
                    for request in ngo.iter('request'): 
                        tiempo_req.append(request.find('time').text)
                        tiempo_min.append(request.find('minTime').text)
                                                  
                    for response in ngo.iter('response'):
                        for receipt in response.iter('receipt'):
                            ID=receipt.find('id').text
        
        
        ##############
        #
        # classical mode, not tested
        #
        ############
        
        #    for queue in proposalClass.iter('classical'): 
        #        #print queue.tag, queue.attrib
        #        #Too= classical.get('tooOption')  #asking if it is a ToO
        #        
        #        for classical in queue.iter('classical'):
        #            #time per partner
        #            partner.append(classical.find('partner').text)
        #            for request in classical.iter('request'): 
        #                tiempo_req.append(request.find('time').text)
        #                tiempo_min.append(request.find('minTime').text)
        #                                          
        #            for response in classical.iter('response'):
        #                for receipt in response.iter('receipt'):
        #                    ID=receipt.find('id').text
        
        
        # Band 3 time: I do not know the partner distribution
                for band3request in queue.iter('band3request'):
                    tiempo_req3.append(band3request.find('time').text)
                    tiempo_min3.append(band3request.find('minTime').text)
        
#        tiempo_req_arr3=np.asarray(tiempo_req3,np.float)
#        tiempo_min_arr3=np.asarray(tiempo_min3,np.float)        



        Requested_instruments=[]
        insturment_mode=[]
        k={}
        d=[]
        Nombre=[]
        for blueprints in root:
            key=blueprints.tag
            #if blueprints.getchildren():
            if list(blueprints): 
                for child in blueprints:
                    if blueprints.tag == 'blueprints':
                        key += '/'+ child.tag
                        k.update({key: child.text})
                        lala=key
                    for children1 in child:
                        #children1.getchildren()
                        list(children1) 
                        #print children1
                        instrument_mode=" "
                        key2=children1.tag
                        for children2 in children1:
                            #children2.getchildren()
                            list(children2) 
                            if children2.tag =='name':
                                
                                Nombre.append(children2.text) 
                                #print children2.tag
                                #print children2.text
                                d.append({key2: children2.text})
                                instrument_mode=d#'\n'
        
        
        
        
        #out_put_file=open(file_out,'w')
        
        #print(f[:-4],piname,pilastname,Title,Nombre,inti,tiempo_req3)

#        print(f[:-4],piname,pilastname,inti,tiempo_req3,Title,Nombre)

#       tiempo_req_arr=np.asarray(tiempo_req,np.float)
#       tiempo_min_arr=np.asarray(tiempo_min,np.float)
        #print "============================================================";
        #print "REQUESTED TIMES";		
        ##print '%20s '
        #print  '                    Time Request       Minimum Time Request'
        #print   ""
        for k in range (len(tiempo_req)):
            if partner[k]=="cl":
                chile=partner[k],
                tiempo_cl=tiempo_req[k]
                #print partner[k],"                ",       tiempo_req[k],"                ",      tiempo_min[k]
        #print(f[:-4],piname,pilastname,inti,chile,tiempo_cl,tiempo_req3,Title,Nombre,partner[k])


#        print  "-------------------------------------------------------";
#        #print "Total";               
        tiempo_req_arr=np.asarray(tiempo_req,np.float)
        tiempo_min_arr=np.asarray(tiempo_min,np.float)
#        
#        print "Total              ",       sum(tiempo_req_arr),"                ",      sum(tiempo_min_arr)
#        
        tiempo_req_arr3=np.asarray(tiempo_req3,np.float)
        tiempo_min_arr3=np.asarray(tiempo_min3,np.float)
#        
#        #print "here" ,tiempo_req_arr3,tiempo_min_arr3
        si=str('No')
        #no=str('No')
        for k in range (len(tiempo_req3)): 
            if tiempo_req_arr3.size:
                banda_3_si=tiempo_req3[k]
                si=str('SI')
            else:
                si=str('NO')

        print(f[:-4],piname,pilastname,inti,chile,tiempo_cl,si,tiempo_req3,Title,Nombre,chile)
 
