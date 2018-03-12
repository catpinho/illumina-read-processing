import os
import gzip
a=os.getcwd()
b=os.listdir(a)

#structure of the sample names: how many parts separated by _ are to be used
parts=2
samplelist=[]

for f in b:
    if "fastq.gz" in f:
        sname="_".join(f.split("_")[:parts])
        if sname not in samplelist:
            samplelist.append(sname)

for s in samplelist:
    print s
    with gzip.open(s+".fastq.gz","ab") as y:
        for fi in b:
            if "fastq.gz" in fi:
                if s == "_".join(fi.split("_")[:parts]):
                    print fi
                    u=gzip.open(fi,"rb")
                    x=u.readline()
                    while x!="":               
                        y.write(x)
                        x=u.readline()
                    u.close()
                
            
        
        
            
            
            
            
                
            
        
        
