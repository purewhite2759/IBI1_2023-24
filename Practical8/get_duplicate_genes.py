#import module
import os
import re

#change the working director
os.chdir('C:/Users/13327/Desktop/schoolworks/classes/IBI/class_materials/practical8/')
#open the original file and create the object file
#open the original file twice to put into two different loops
fafile1=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fafile2=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fout=open('duplicate_genes.fa','w')

#create dictionary about gene name and sequence
#the dictionary is used to find right sequence of certain gene
dic={}
gene_seq=''
for line in fafile1:
    if line.startswith('>'):
        gene_name1=''.join(re.findall(r'^(\S+)',line))
        gene_seq=''#record as a new sequence when there comes to another gene
    else:
        gene_seq=gene_seq+line.strip()#create the gene sequence without '\n'
    dic[gene_name1]=gene_seq

#find the object genes and record them to the object file
for lines in fafile2:
    if re.search('duplication',lines):
        gene_name2=''.join(re.findall(r'^(\S+)',lines))
        fout.write(gene_name2+'\n')
        fout.write(dic[gene_name2]+'\n')

fout.close()