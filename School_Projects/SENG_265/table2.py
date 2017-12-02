"""
Gillian Bryson
V00880054
"""

import re
import operator
import sys
import select
print ("hello")
args=sys.argv
#text= args[1]#replace this with a better way !!
lines=[]
#print(args[1]);

for line in sys.stdin:# open file and
	lines.append(line)#lines is an array of lines of words
words=[] # words holder
print_me = False
tbl_cnt=1# if there is no table this number will never be printed anyways so we can assume it can start at 1
print_lines=[]
print_words=[]

for line in lines:
    #print(line)
    #print("START FOUND: "+line)
    if '<table' in line:
        #print('TABLE %d:'%tbl_cnt)
        if tbl_cnt >1:
            print_lines.append([""])
        print_lines.append(['TABLE %d:'%tbl_cnt])
        tbl_cnt +=1

    if (("<tr") in line.lower()):
        print_me=True
    if print_me:
        #print('line:'+line.strip());
        words=re.split('(<[^>]*>)',line.strip())
        # print('words:',end="")
        # print(words)
        word_cnt_a=len(words);
        #print ("hello") #this line was here before i started editing
		print ("hello") # i wanted to add a print line
		
        for word in range(0,word_cnt_a-1):
            if (not(words[word].endswith('>')) and (not(words[word].startswith('<t')))):
                if not ((word==0) or (word==(word_cnt_a-2))):
                    if ('<t' in words[word-1].lower())and('</t' in words[word+1].lower()):
                        if (words[word].replace(" ","")==''):
                            print_words.append('')

                        else:
                            print_words.append(' '.join((words[word].strip()).split()))
    if (("</tr") in line.lower()) and (print_me):
        print_lines.append(print_words)
        print_words=[]
        print_me=False
#print(print_lines)
topLen=len(print_lines[1])
for print_words in print_lines:
	wrd_cnt=len(print_words)
	if(wrd_cnt<=0):
		continue
	#print (topLen)
	for place in range(0,topLen):
		#print(place)
		if (place>=wrd_cnt):
			if(place==topLen-1):
				print();
			else:
				print(',',end="")
		elif place == topLen-1:
			print (print_words[place])
			if ('TABLE' in print_words[place]):
				print (print_words[place])
				break
		else:
			if ('TABLE' in print_words[place]):
				print (print_words[place])
				break
			else:
				print(print_words[place]+",",end="")
