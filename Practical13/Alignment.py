#import modules
import os
import blosum as bl #used to read BLOSUM62 matrix

#input files
os.chdir('C:/Users/13327/Desktop/schoolworks/classes/IBI/class_materials/practical13/')
#read sequenes from .fa files
fa_human=open('SLC6A4_HUMAN.fa')
fa_mouse=open('SLC6A4_MOUSE.fa')
fa_rat=open('SLC6A4_RAT.fa')
human_str=''
mouse_str=''
rat_str=''
for line in fa_human:
    if not line.startswith('>'):
        human_str=human_str+line.strip()
for line in fa_mouse:
    if not line.startswith('>'):
        mouse_str=mouse_str+line.strip()
for line in fa_rat:
    if not line.startswith('>'):
        rat_str=rat_str+line.strip()
#create a dictionary, which do help to print the output
dir={human_str:'SC6A4_HUMAN',
     mouse_str:'SC6A4_MOUSE',
     rat_str:'SC6A4_RAT'}
#read BLOSUM62 matrix
matrix=bl.BLOSUM(62)

#compare each amino acid and print output
def alignment(seq1_str,seq2_str):
    '''
    input: two sequences to be compared
    code: calculate the alignment score according to BLOSUM62 matrix, and give the percentage of identity
    output: the alignment score and the percentage of identity
    '''
    seq1=list(seq1_str)
    seq2=list(seq2_str)
    score=0 #to record the alignment score
    identity=0 #to record the number of identical amino acids
    index=min(len(seq1),len(seq2))
    for i in range(index):
        score+=matrix[seq1[i]][seq2[i]]
        if seq1[i]==seq2[i]:
            identity+=1
    percentage=identity/index
    return print('Seq1:',dir[seq1_str],'\nSeq2:',dir[seq2_str],'\nScores:',score,'\nPercentage of identity:',percentage)

alignment(mouse_str,rat_str)