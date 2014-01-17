Nine={}
for i in range(0,256):
	Nine[i]='0'+str('{0:08b}'.format(i))
for key,value in Nine.iteritems():
	print str(key)+" "+value
