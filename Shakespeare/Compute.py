import re
words=['that','with','your','this','have','thou','will','thee','shall','That','What','from','good','what','love','more','lord','would','Enter','them','they','their','here','well','know','hath','like','come','then','there','make','than','upon','should','which','were','must','KING','King','such','when','This','these','some','mine','heart','father','time','Exeunt','give','speak','take','much','With','most','think','Exit','Come','Thou','never','Which','tell','life','hand','When','death','great','doth','night','hear','made','true','very','again','cannot','There','fair','other','Then','away','where','been','eyes','world','Lord','look','sweet','Where','blood','done','SCENE','name','Your','Here','down','call','before','fear','FIRST','honour','leave','thus','brother','They','comes','ever','noble','Well','heaven','lady','better','could','into','poor','DUKE','Good','pray','being','house','Duke','nothing','many','both','hast','head','myself','bear','dead','find','master','part','word','still','wife','Will','live','little','Prince','Shall','first','stand','those','SECOND','friends','soul','against','every','might','Have','gone','place','long','show','COPIES','ELECTRONIC','DISTRIBUTED','himself','Caesar','best','GLOUCESTER','friend','thine','keep','Than','daughter','face','woman','none','QUEEN','dear','till','France','tongue','words','young','answer','full','though','mother','peace','king','else','fool','whose','hold','HENRY','LORD','forth','Queen','once','stay','bring','said','thought','another','enter','mind','therefore','about','FALSTAFF','indeed','thing','unto','three','hope','matter','From','sword','John','Rome','rest','gentle','within','back','after','heard','RICHARD','cause','Aside','dost','whom','truth','fall','home','play','nature','please','Master','England','Give','Upon','lords','madam','right','morrow','turn','thousand','Grace','even','husband','hands','faith','earth','hence','hour','makes','meet','state','news','things','ring','fellow','kill','BRUTUS','power','PAGE','came','crown','gentleman','ANTONY','without','CLOWN','shame','Hath','enough','hither','mean','rather','does','shalt','since','false','follow','thank','body','gods','reason','help','OTHELLO','honest','youth','Would','grace','tears','IAGO','welcome','fight','wrong','WILLIAM','kind','Look','yourself','seen','sure','Therefore','means','fortune','mistress','fire','YORK','SERVANT','light','sent','court','last','lost','near','spirit','only','arms','Even','yours','wish','letter','CLEOPATRA','TIMON','WARWICK','pardon','sleep','Some','horse','strange','swear','together','break','present','same','thoughts','work','high','York','cousin','itself','left','Whose','devil','Though','OTHERS','alone','business','prove','says','Lear','Henry','THIS','wilt','SYRACUSE','breath','through','villain','child','return','GUTENBERG','PROJECT','Antony','COMPLETE','SHAKESPEARE','told','ETEXT','THAT','TIME','beauty','found','lies','CHARGES','MESSENGER','More','PROVIDED','SUCH','These','WORKS','bloody','LIBRARY','WITH','BENEDICTINE','COLLEGE','COMMERCIAL','COMMERCIALLY','COPYRIGHT','DISTRIBUTION','DOWNLOAD','ILLINOIS','INCLUDES','LONG','MACHINE','MEMBERSHIP','ONLY','PERMISSION','PERSONAL','PROHIBITED','READABLE','SERVICE','USED','VERSION','WORLD','YOUR','send','service','gave','half','FORD','ROSALIND','less','talk','gold','people','foul','under','days','grief','Before','land','kiss','seek','care','desire','MACBETH','times','Take','self','Pray','Till','beseech','knows','pity','royal','ANTIPHOLUS','purpose','charge','company','seem','looks','GENTLEMAN','Majesty','lose','worth','Speak','sight','Were','JOHN','Edward','between','dare','over','worthy','late','loves','proud','sister','Most','Farewell','born','each','Kent','uncle','wear','strong','cold','queen','Highness','Like','field','lives','years','DROMIO','happy','brought','general','thyself','Tell','believe','gracious','known','sorrow','free','given','holy','maid','others','read','serve','Marry','further','marry','Lady','Madam','Richard','country','grave','money','need','Brutus','MENENIUS','Warwick','foot','side','Thus','hang','wind','Alas']
Seventeen={}
Nine={}
FinalString=""
for i in range(0,len(words)):
	words[i]=words[i].strip()
i=0
for w in words:
	Seventeen[w]=('1'+'{0:016b}'.format(i)).strip()
	i+=1
for i in range(0,256):
	Nine[i]=('0'+str('{0:08b}'.format(i))).strip()
space=Nine[32]
InputData=""
while True:
    try:
        line = raw_input()
    except:
        break
    InputData+=line+"\n"
Data=InputData.split()

for s in Data:
	if s.isalpha():
		if s in Seventeen:
			FinalString+=Seventeen[s]
		else:
			for x in s:
				FinalString+=Nine[ord(x)]
	else:
		for x in s:
			FinalString+=Nine[ord(x)]
	FinalString+=space
FinalString=FinalString[0:len(FinalString)-len(space)]
#print len(Seventeen)
#for x,y in Seventeen.iteritems():
#	print x+"\t"+y
print FinalString

