import re
words=
Seventeen={}
Nine={}
Result=""
for i in range(0,len(words)):
	words[i]=words[i].strip()
i=0
for w in words:
	Seventeen[w]=('1'+'{0:016b}'.format(i)).strip()
	i+=1
for i in range(0,256):
	Nine[i]=('0'+str('{0:08b}'.format(i))).strip()
Data=""
while True:
    try:
        Data+= raw_input()+'\n'
    except:
        break
#Data=Data.strip('\n')
Data=re.split(r'([^a-zA-Z])',Data)
FinalString=[]
length=len(Data)
i=0
while i<length:
	if not(len(Data[i])==0):
		flag=0
		if (i+2)<length:
			Temp=(Data[i]+Data[i+1]+Data[i+2])
			if (Temp in Seventeen):
				FinalString.append(Seventeen[Temp])
				flag=1
				i+=2
		if (flag==0):
			if (Data[i] in Seventeen):
				FinalString.append(Seventeen[Data[i]])
			else:
				for x in Data[i]:
					FinalString.append(Nine[ord(x)])
	i+=1
print len(Seventeen)
for x,y in Seventeen.iteritems():
	print (x+"\t"+y)
print ''.join(FinalString)

