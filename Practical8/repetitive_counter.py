#find number of certain repetitive element
#import module
import re

seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
#find the repeat elements
repeat_element1=re.findall('GTGTGT',seq)
repeat_element2=re.findall('GTCTGT',seq)
#count the number of repeat elements
amount=len(repeat_element1)+len(repeat_element2)

print('Taking account of possible overlapping instances, there are',amount,'repeat elements')
