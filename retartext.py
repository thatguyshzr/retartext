import re
from random import randint

# text= '''In this grave hour, perhaps the most fateful in our history,
# I send to every household of my peoples, 
# both at home and overseas, this message, 
# spoken with the same depth of feeling for each one of you, 
# as if I were able to cross your threshold and speak to you myself.'''

def lower_punc(text):
	text= text.lower()
	text= re.sub(r'[^\w\s]', '', text)
	return text

def replacer(text):
	words= {'are':'r', 'you':'u', 'your':'ur', 'the':'da', 'and':'n',
	'message':'msg', ' to ': ' 2 ', 'every':'evry',
	'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
	'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
	for word, replacement in words.items():
		text= text.replace(word, replacement)
	return text

def remove_vowel(text):
	text = lower_punc(text)
	text = replacer(text)
	temp_text= ''
	for i in text.split():
		if len(i) > 2:			# dont work for small words like "to", "at"
			if re.match('[^aeiou]+[aeiou]', i):	# consonant-vowel
				temp_text+= re.sub('[aeiou]', '', i) + " "	# remove vowel
			else:
				temp_text+= i + ' '
		else:
			temp_text+= i + ' '

	return temp_text
	
def random_upper(text):
	text = remove_vowel(text)
	temp_text = ''
	for i in text:
		x= randint(0,3)		# probability of uppercase 1/4
		if x == 2:
			temp_text += i.upper()
		else:
			temp_text += i
	return temp_text

def add_emoji(text):
	text = random_upper(text)
	emoji= ["\U0001F606", '\U0001F600', "\U0001F603",
	"\U0001F604", "\U0001F601", "\U0001F605"]
	temp_text= ''
	for i in text:
		x= randint(0,len(emoji))
		if i == ' ':
			if x == 2 | x == 3:		# probability of emoji 2/6
				temp_text+= emoji[randint(0,len(emoji)-1)] + " "
			else:
				temp_text+=i
		else:
			temp_text+= i

	return temp_text

# print(add_emoji(text))