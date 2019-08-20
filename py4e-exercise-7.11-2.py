file_name = str.lower(input('What is the name of the file to read? '))
search_string = input('What is the string you are looking for: ')

try:
    fhand = open(file_name)

except:
    print('Please choose an existing file')
    exit()
count = 0
spam_conf = 0
avg_spam_conf = 0
for line in fhand:
    if line.startswith(search_string):
        count = count + 1
        line = float(line[19:])
        spam_conf = line + spam_conf
        avg_spam_conf = spam_conf / count
print('The average SPAM confidence score is: %f' % avg_spam_conf)