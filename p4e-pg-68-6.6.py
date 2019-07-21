try:
	letter = input('Enter something: ')
	lowercase_letter = letter.lower()  #<----   Taking var letter and converting to lower case without having to use 'str.lower' method
	word = input('Enter letter you want counted: ')
	lowercase_word = word.lower()  #<----   Taking var word and converting to lower case without having to use 'str.lower' method



	def count(letter):
		counter = 0
		for letter_counter in lowercase_letter:
			if letter_counter == lowercase_word:
				counter = counter + 1
				continue
		print(counter)

	count(lowercase_letter)

except:
	print('Please enter in something valid')



