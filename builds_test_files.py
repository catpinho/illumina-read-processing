#this script creates small (5000 reads) fastq files from real data that allow manipulating, observing and script testing on them
#it takes a folder of files with real gzipped data and creates as many fastq.gz files as in that folder
import os
import gzip
a=os.getcwd()
b=os.listdir(a)
for f in b:
    if ".fastq.gz" in f:
        u=gzip.open(f,"rb")
        with gzip.open(f.split(".fastq.gz")[0]+"_small.fastq.gz","wb") as z:
            for l in range(20000):
                z.write(u.readline())
        z.close()
                
            
        
        
            
            
            
            
                
            
        
        
