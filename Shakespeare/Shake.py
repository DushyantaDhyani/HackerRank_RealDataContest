import operator
import re
import nltk
import string
from nltk.book import *
from nltk.collocations import *
from nltk.util import ngrams
from nltk.corpus import PlaintextCorpusReader
FinalString="["
Mapper=open('Output/KeyFile.txt','w')
raw=open("Input/ShakeFull.txt",'r').read()
corpus_root = '/home/alphacentauri/Docs/HackerRank/Contest/RealData/Shakespeare/Input'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
words=wordlists.words('ShakeFull.txt')
text=nltk.Text(words)
fdist=FreqDist(words)
freqtokens=fdist.keys()
prioritylist=[w for w in freqtokens if (w.isalpha() and len(w)>1)]

printset=set(string.ascii_letters+string.digits).union(set("[](){}:,.-_!;/\+=*%#@~ "))
################# ADDING BIGRAMS ###################################
NewRaw=re.split(r'[^a-zA-Z]',raw)
NewRaw=[x.strip() for x in NewRaw if len(x)>0]
N=3
sixgrams = ngrams(NewRaw, N)
Data={}
for grams in sixgrams:
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
prioritylist+=NewData[0:(65500-len(prioritylist))]
#####################################################################
print len(prioritylist)
for c in prioritylist:
	FinalString+="'"+c+"'"+","
FinalString=FinalString[0:len(FinalString)-1]
Mapper.write(FinalString+"]")	

