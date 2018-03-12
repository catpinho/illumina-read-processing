#this script removes everything in a read that appears prior to the restriction site.
#it is to be used in gzipped fastq files
#this is useful to remove barcodes in RADseq data for subsequent processing with stacks or other software
#the outputs are:   1) new fastq files with extension ("_nobarcode.fastq.gz")(the remaining name is the same)
#                   2) one file with reads that are discarded (where the restriction site was not found - discards.fq.gz)
#                   3) a file with sizes for the retained reads
#edit the restriction site here:
restriction_site="TGCA"
import os
import gzip
a=os.getcwd()
b=os.listdir(a)
d=gzip.open("discards.fq.gz","ab")
sizes=file("sizes.txt","a")
for f in b:
    if ".fastq.gz" in f:
        u=gzip.open(f,"rb")
        x=u.readline()
        while x!="":
            read=x+u.readline()+u.readline()+u.readline()
            if read.split("\n")[1].find(restriction_site)!=-1:
                read2=read.replace(read.split("\n")[1],read.split("\n")[1][read.split("\n")[1].index(restriction_site):])
                sizes.write(str(len(read.split("\n")[1][read.split("\n")[1].index(restriction_site):]))+"\n")
                with gzip.open(f.split(".fastq.gz")[0]+"_nobarcode.fastq.gz","ab") as y:
                    y.write(read2)
            else:
                d.write(read)
            x=u.readline()
                
            
        
        
            
            
            
            
                
            
        
        
