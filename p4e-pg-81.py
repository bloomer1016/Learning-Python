prompt = str.lower(input('What is the name of the file to read? '))
try:
    fhand = open(prompt)

except:
    print('Please choose an existing file')
    exit()
count = 0
for line in fhand:
    if line.startswith('From:'):
        line = line.rstrip()
        count = count + 1
        #print(line)
print('Total count in file: %s' %prompt, 'is %d.' %count)

