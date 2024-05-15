import datetime #to test run time
import os
import xml.dom.minidom as xdm
import xml.sax
from xml.sax.xmlreader import AttributesImpl
import matplotlib.pyplot as plt #to draw figures

#input go_obo.xml
#calculates the number of GO terms within each of molecular function, biological process and cellular components using the DOM and SAX APIs
#change directory 
os.chdir('C:/Users/13327/Desktop/schoolworks/classes/IBI/class_materials/practical14/')

#for the DOM API
starttime1=datetime.datetime.now() #record the start time of the first API

DOMTree=xdm.parse('go_obo.xml')
ROOT=DOMTree.documentElement
term=ROOT.getElementsByTagName('term')
MF_counter=0
BP_counter=0
CC_counter=0
for terms in term:
    if terms.getElementsByTagName('namespace')[0].firstChild.nodeValue=='molecular_function':
        MF_counter+=1
    elif terms.getElementsByTagName('namespace')[0].firstChild.nodeValue=='biological_process':
        BP_counter+=1
    elif terms.getElementsByTagName('namespace')[0].firstChild.nodeValue=='cellular_component':
        CC_counter+=1

endtime1=datetime.datetime.now() #record when this API ends
runtime1=endtime1-starttime1 #calculate the run time of the first API
print('*****DOM API*****')
print('the number of GO terms within molecular function:',MF_counter)
print('the number of GO terms within biological process:',BP_counter)
print('the number of GO terms within cellular componet:',CC_counter)
print('run time:',runtime1)

#create figure according to the results
term_name=['molecular function','biological process','cellular componet']
frequency1=[MF_counter,BP_counter,CC_counter]
plt.figure(1)
plt.bar(term_name,frequency1)
plt.ylabel('frequency')


#for the SAX API
starttime2=datetime.datetime.now() #record the start time of the second API
MF=[] #used to record number of terms
BP=[]
CC=[]
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.namespace=''
        self.id=''
    def startElement(self, tag, attributes):
        self.CurrentData=tag
    def endElement(self, tag):
        if self.namespace=='molecular_function':
            MF.append(1)
        if self.namespace=='biological_process':
            BP.append(1)
        if self.namespace=='cellular_component':
            CC.append(1)
    def characters(self, content):
        if self.CurrentData=='namespace':
            self.namespace=content
        if self.CurrentData=='id':
            self.id=content

parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler=GOHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

endtime2=datetime.datetime.now() #record when this API ends
runtime2=endtime2-starttime2 #calculate the run time of the second API

print('*****SAX API*****')
print('the number of GO terms within molecular function:',len(MF))
print('the number of GO terms within biological process:',len(BP))
print('the number of GO terms within cellular componet:',len(CC))
print('run time:',runtime2)

#create figure according to the results
frequency2=[len(MF),len(BP),len(CC)]
plt.figure(2)
plt.bar(term_name,frequency2)
plt.ylabel('frequency')

plt.show()
plt.clf()
#on my computer, SAX API is faster