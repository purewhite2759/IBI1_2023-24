#import module
import os
import re

#most parts are the same as the second task
os.chdir('C:/Users/13327/Desktop/schoolworks/classes/IBI/class_materials/practical8/')
repeat_seq=input("repetitive sequences ('GTGTGT' or 'GTCTGT'):")#input repeat sequence
fafile1=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fafile2=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#name the new file
if repeat_seq=='GTGTGT':
    fout=open('GTGTGT_duplicate_genes.fa','w')
else:
    fout=open('GTCTGT_duplicate_genes.fa','w')

dic={}
gene_seq=''
for line in fafile1:
    if line.startswith('>'):
        gene_name1=''.join(re.findall(r'^(\S+)',line))
        gene_seq=''
    else:
        gene_seq=gene_seq+line.strip()
    dic[gene_name1]=gene_seq

for lines in fafile2:
    if re.search('duplication',lines):
        gene_name2=''.join(re.findall(r'^(\S+)',lines))
        fout.write(gene_name2+'\n')
        repeat_element=re.findall(repeat_seq,dic[gene_name2])#find repeat elements
        amount=len(repeat_element)#count repeat elements
        fout.write(str(amount))#write the number into the file
        fout.write(' repeat elements\n')
        fout.write(dic[gene_name2]+'\n')

fout.close()