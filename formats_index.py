#this script removes the "+" that illumina software leaves on the double index read headings
#takes a folder of fastq.gz files and calls them noplus.fastq.gz

import os
import gzip
a=os.getcwd()
b=os.listdir(a)
for f in b:
    if ".fastq.gz" in f:
        u=gzip.open(f,"rb")
        with gzip.open(f.split(".fastq.gz")[0]+"_noplus.fastq.gz","wb") as z:
            x=u.readline()
            while x!="":
                y=x.split(":")[-1]
                readhead=x.replace(y,y.replace("+",""))
                read=readhead+u.readline()+u.readline()+u.readline()
                z.write(read)
                x=u.readline()
                
            
        
        
            
            
            
            
                
            
        
        
