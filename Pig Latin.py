print "Welcome, Human, to Pig Latin!"

original=raw_input("Enter a valid English word:")
suf='ay'
if(original.isalpha() and len(original)>0):
	word=original.lower()
	first=word[0]
	new_word=word+first+suf
	new_word=new_word[1:len(new_word)].capitalize()

	print "The Pig Latin equivalant of %s is %s" %(original,new_word)
else:
	print "Please enter a valid English word."