

import re
import operator

## Read the log.txt file and Clean the data into columns using Regular Expression

print("Reading log.txt file .... ")

p = re.compile(r" - - \[|\] \"POST | HTTP/1.0\" |\] \"GET | -|\" |\] \"HEAD ")
with open("../log_input/log.txt","r",encoding='latin-1') as f:
    data = f.readlines()

## Dictionary for the hosts and resources columns
    
print("Creating dictionary for hosts and resources .... ")

hosts ={}
resources ={}
for line in data:    
    line=line.strip('\n')
    words = p.split(line)    
    if words[0] in hosts:
        hosts[words[0]]+=1
    else:
        hosts[words[0]]=1
    if words[3]!='/':    
        if words[3] in resources:            
            tmp=words[4].split()            
            if len(tmp)==1 or len(tmp)==0:
                bytesSent=0
            else:
                bytesSent=int(tmp[1])            
            resources[words[3]]=resources[words[3]] + bytesSent
        else:           
            tmp=words[4].split()            
            if len(tmp)==1 or len(tmp)==0:
                bytesSent=0
            else:
                bytesSent=int(tmp[1])            
            resources[words[3]]=bytesSent

##########################################
    ## Feature 1 ##
##########################################

print("Working on Feature 1 .... ")

sorted_hosts = sorted(hosts.items(),key=lambda x: (-x[1], x[0]))
with open('../log_output/hosts.txt', 'w') as f:
    for k, v in sorted_hosts[:10]:
    #print ("{key},{value}".format(key=k,value=v))    
        f.write("{key},{value}".format(key=k,value=v)+"\n")     




##########################################
    ## Feature 2 ##
##########################################

print("Working on Feature 2 .... ")

sorted_resources = sorted(resources.items(),key=lambda x: (-x[1], x[0]))
with open('../log_output/resources.txt', 'w') as f:
    for k, v in sorted_resources[:10]:
        #print ("{key},{value}".format(key=k,value=v))
        f.write("{key}".format(key=k)+"\n")


