count = 0
total_sum = 0
avg_sum = 0

while True:
	prompt = input('Enter a number - Type "done" to quit: ')
	try:
		if prompt == 'done' or prompt =='DONE' or prompt == "Done":
			if count == 0:
				print('Nothing has been entered. Quiting now.')
				break
			elif count > 0:
				print('We are done! Here are the results.', 'Total sum:',total_sum, 'Count:',count, 'Avgerage:',avg_sum)
				break
		total_sum = int(total_sum) + int(prompt)
		count = int(count) + 1
		avg_sum = int(total_sum) / int(prompt)

	except:
		print('Please enter a number ONLY! Try again.')