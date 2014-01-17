import nltk
from nltk.util import ngrams
from nltk.corpus import PlaintextCorpusReader
import re
raw=open('Input/ShakeFull.txt').read()
Mapper=open('Output/KeyFile.txt','w')
prioritylist=[]
FinalString="["
for n in range(4,5):
	NewRaw=re.split(r'([^a-zA-Z])',raw)
	NewRaw=[x.strip() for x in NewRaw if len(x)>0]
	Ngrams = ngrams(NewRaw, n)
	Data={}
	for grams in Ngrams:
			Flag=False
			for x in grams:
				if not(x.isalpha()):
					Flag=True
					break
				if not(Flag):
					temp=' '.join(grams)
			  		try:
					 	Data[temp]+=1;
					except:
						Data[temp]=1
	NewData=sorted(Data, key=Data.get, reverse=True)
	prioritylist=NewData[0:34000]
print len(prioritylist)
for c in prioritylist:
	FinalString+="'"+c+"'"+","
FinalString=FinalString[0:len(FinalString)-1]
Mapper.write(FinalString+"]")	

