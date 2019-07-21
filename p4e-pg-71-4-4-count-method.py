try:
	letter = str.lower(input('Enter something: '))
	word = str.lower(input('Enter letter you want counted: '))

	def count(letter,word):
		letter.count(word)
		print(letter.count(word))

	count(letter,word)

except:
	print('Try again')