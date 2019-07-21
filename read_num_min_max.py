prompt = 0 
large = None 
small = None 

while True:
	prompt = input('Enter a number - Type "done" to quit: ')
	if prompt == 'done' or prompt =='DONE' or prompt == "Done" or prompt =="":
		print('Here are the results.', 'Min:',small, 'Max:',large)
		break

	try:
		num = float(prompt)
	
	except:
		print('Invalid input')
		continue
	
	if small is None or num < small:
		small = num
	if large is None or num > large:
		large = num