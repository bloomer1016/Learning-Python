string_input = str.lower(input("Please enter something: "))
string_looking = str.lower(input('What are you looking for?: '))
string_end = str.lower(input('What does it end with?: '))
possible_num = str.lower(input('Looking for a number (Y or N)?: '))

if possible_num == 'y':
	pos_string_var_start = float(string_input.find(string_looking))
	pos_string_var_end = float(string_input.find(string_end))
	final_string = string_input[pos_string_var_start:pos_string_var_end+1]
	print(final_string)

elif possible_num == 'n':
	pos_string_var_start = string_input.find(string_looking)
	pos_string_var_end = string_input.find(string_end)
	final_string = string_input[pos_string_var_start:pos_string_var_end+1]
	print(final_string)