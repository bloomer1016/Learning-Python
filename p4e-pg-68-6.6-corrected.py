try:
	#letter = str.lower(input('Enter something: '))
	letter = input('Enter something: ')
	lowercase_letter = letter.lower()  #<----   Taking var letter and converting to lower case without having to use 'str.lower' method
	#word = str.lower(input('Enter letter you want counted: '))
	word = input('Enter letter you want counted: ')
	lowercase_word = word.lower()  #<----   Taking var word and converting to lower case without having to use 'str.lower' method

	def count(lowercase_letter):
		counter = 0		#made this a local variable to the function
		for letter_counter in lowercase_letter:
			if letter_counter == lowercase_word:
				counter = counter + 1
				#continue --> Do not need this anymore
		print(counter) #--> REM'ing this out since it is no longer needed in the function itself

	count(lowercase_letter)
	
except:
	print('Please enter in something valid')