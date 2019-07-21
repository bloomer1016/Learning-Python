prompt = input('Enter number of hours worked: ')
rate = input('Enter pay rate: ')

try:

	def comp_pay(prompt, rate):
		if int(prompt) > 40:
			overtime_pay = (int(prompt) * int(rate)) * 1.5
			print('You worked overtime! Your pay is: ', overtime_pay)
			return overtime_pay

		elif int(prompt) <= 40:
			non_overtime = int(prompt) * int(rate)
			print('You did not work overtime! Your pay is: ', non_overtime)
			return non_overtime

	comp_pay(prompt, rate)

except:
	print('You must enter numbers only!')