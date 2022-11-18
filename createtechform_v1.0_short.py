#!/usr/bin/env python

##
#
# Based in createformv12.pl  and Gem_stats.py
#
# Marcelo Mora   mmora@astro.puc.cl/mmmrage@gmail.com
# Customized for 2017A CL: i.e. No classical, no exchange, no Visitor.   
# 
# I do not know how to split band 3 time among partners
#
## 
 

########################################
#
# Execute on the directory where the .xml files are located the following line:
#
# python createtechform_v1.0.py
# 
#
#
#
########################################

import xml.etree.ElementTree as ET
import os,sys,string
import numpy as np
from lxml.etree import parse as lparse

#read each xml file into an array
files= [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f.endswith(('.xml')):
        print f
        #change the output .txt
        file_out=f[:-3]+'txt' 
        print file_out




         
        ltree= lparse(f)
        tree = ET.parse(f) #setup ETread
        root = tree.getroot() #define root 
        #get PI name
        # .encode('utf-8') used to avoid accents and other characters
        for pi in root.iter('pi'):
            pilastname= pi.find('lastName').text.encode('utf-8')
            piname=pi.find('firstName').text.encode('utf-8')
            email=pi.find('email').text

        for proposal in root.iter('proposal'):
            Title=proposal.find('title').text
        
        
        
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
        
        



        Requested_instruments=[]
        insturment_mode=[]
        k={}
        d=[]
        Nombre=[]
        for blueprints in root:
            key=blueprints.tag
            if blueprints.getchildren(): 
                for child in blueprints:
                    if blueprints.tag == 'blueprints':
                        key += '/'+ child.tag
                        k.update({key: child.text})
                        lala=key
                    for children1 in child:
                        children1.getchildren()
                        #print children1
                        instrument_mode=" "
                        key2=children1.tag
                        for children2 in children1:
                            children2.getchildren()
                            if children2.tag =='name':
                                
                                Nombre.append(children2.text) 
                                #print children2.tag
                                #print children2.text
                                d.append({key2: children2.text})
                                instrument_mode=d#'\n'
        
        
        
        
        out_put_file=open(file_out,'w')
        
        #print instrument_mode
        
        
        #print piname, pilastname
        #print email
        #print Title
        #print Time_band12
        #print Too
        #print partner
        #print IDpri
        #
        #     
        
        # output to a file
        
        temp=sys.stdout                   
        sys.stdout =open(file_out,'w')       # redirect all output to the file
                
                
        
        


        print  "============================================================ "
        
        print  "Gemini Partner (AR/AU/BR/CA/CL/GS/US/UH): ", '/'.join(partner) 
        #for i in range (len (partner)): print partner[i]+" "
        
        print  "NGO Proposal ID:" + ID
        
        print  "Assessor Code: ";
        
        print  "Title:" + Title
        
        print  "PI: " +piname, pilastname
        print  "PI email:"+email
        print  "============================================================ ";

        
        print  "OBSERVATIONAL DETAILS ";
        
        print  "Mode:"
        
        #print  "Telescope: $telescope[$j] ";
        
        print  "Instrument(s)/Mode(s):" 
        for n in range(len (Nombre)):
            print Nombre[n]
        #print d
        
        #print  "LASER: $laser[$j] ";
        
        print  "ToO:", Too
        #print  "[Please check whether target is transient and flag here if necessary.] ";
         
        #print  "Suitable for poor weather: ";
         #                 
        print "============================================================";
        print "REQUESTED TIMES";		
        #print '%20s '
        print  '                    Time Request       Minimum Time Request'
        print   ""
        for k in range (len(tiempo_req)):
            print partner[k],"                ",       tiempo_req[k],"                ",      tiempo_min[k]
        print  "-------------------------------------------------------";
        #print "Total";               
        tiempo_req_arr=np.asarray(tiempo_req,np.float)
        tiempo_min_arr=np.asarray(tiempo_min,np.float)
        
        print "Total              ",       sum(tiempo_req_arr),"                ",      sum(tiempo_min_arr)
        
        tiempo_req_arr3=np.asarray(tiempo_req3,np.float)
        tiempo_min_arr3=np.asarray(tiempo_min3,np.float)
        
        #print "here" ,tiempo_req_arr3,tiempo_min_arr3
        
        if tiempo_req_arr3.size:
            print "-------------------------------------------------------";
            print  "BAND 3 REQUESTED TIMES:";	
            for k in range (len(tiempo_req3)):
                print "Total                ",       tiempo_req3[k],"                ",      tiempo_min3[k]
            print "-------------------------------------------------------";
        else:
            print "-------------------------------------------------------";
            print  "BAND 3 NOT REQUESTED";	
        
        
        
        print  "============================================================ \n";
        print  "DETAILED ASSESSMENT ";
        print  " ";
        print  " ";
        print  " ";
        print  " ";
        print  " ";
        print  " ";
        
#        print  "============================================================ \n";
        sys.stdout.close()                          # closing the file
        sys.stdout=temp                   
        


 
