"""
Gillian Bryson
"""
#Imports
import re
import operator
import sys

args=sys.argv

lines=[]#will hold lines from file

for line in sys.stdin:
	lines.append(line)
tbl_cnt=1;#if there are no tables this will never be used so we can assume ther will be at least 1 table

print_lines=[]#list of list of words to print
print_words=[]#list of words to print

print_me=False
for line in lines:
	if '<table' in line.lower():
		#print('found table')
		print_lines.append(['TABLE %d:'%tbl_cnt])
		tbl_cnt+=1
	if '<tr' in line.lower():
		print_me=True
	if print_me:
		split_line=re.split('(<t[^>]*>)|(</t[^>]*>)|(<T[^>]*>)|(</T[^>]*>)',line.strip())
		# list(filter(lambda a: a != None, split_line))
		while None in split_line:
			split_line.remove(None)

		spLnLen=len(split_line)
		# print('pre: ',end="")
		#print(split_line)
		#print(spLnLen)
		a=0
		while a< spLnLen-1:
			#print(a)
			#print(a,end=" ")
			#print(spLnLen)
			#print(split_line[a])
			#print(split_line[a])

			if (split_line[a].strip()=='')and(a==0):
				split_line.pop(a)
				spLnLen=len(split_line)
				a=0
				continue
			#print('\nbefore: '+split_line[a-1]+" middle: "+split_line[a]+" after: "+split_line[a+1]+"\n")
			if (split_line[a].strip()=='') and (not('<t' in split_line[a-1]) or not('</t' in split_line[a+1]) ):
				#print('popping: '+split_line[a]+" at %d"%a)
				split_line.pop(a)
				spLnLen=len(split_line)
				a=0
				continue
			a+=1
		if (split_line[len(split_line)-1]==''):# and ('</t' in split_line[len(split_line)-2])
			split_line.pop(len(split_line)-1)
			#a=-1
		#print('post: ',end="")
		#print(split_line)
		for word in split_line:
			#print(word)
			word=word.strip()
			if not(('<t' in word.lower()) or('</t' in word.lower())):
					print_words.append(' '.join(word.strip().split()))
			elif ('</tr' in word.lower()):
					# print('appending')
					# print(print_words)
					print_lines.append(print_words)
					print_words=[]
					print_me=False
# while [''] in print_lines:
# 	print_lines.remove([''])
#print(print_words)
lnLen=len(print_lines[1])
reNum=False
for print_words in print_lines:
	#print(print_words)
	myLen=len(print_words)
	if myLen<=0:
		continue
	if (myLen==1)and(print_words[0]==""):
		# print()
		continue
	if reNum:
		lnLen=len(print_words)
		reNum=False
	if 'TABLE' in print_words[0]:
		if '1:' in print_words[0]:
			print(print_words[0])
		else:
			print()
			print(print_words[0])
		continue
	#print(myLen)
	for place in range(0,lnLen):
		#print('place %d'%place)
		if (place>=myLen):
			if(place==lnLen-1):
				print("")
			else:
				print(',',end="")
		elif place == lnLen-1:
			#print('end found')
			print(print_words[place])
		else:
			print(print_words[place]+",",end="")
