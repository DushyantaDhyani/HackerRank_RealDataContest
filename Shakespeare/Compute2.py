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
for s in Data:
	if not(len(s)==0):
		if s in Seventeen:
			FinalString.append(Seventeen[s])
		else:
			for x in s:
				FinalString.append(Nine[ord(x)])
print len(Seventeen)
for x,y in Seventeen.iteritems():
	print x+"\t"+y
#print ''.join(FinalString)

