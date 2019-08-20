prompt = str.lower(input('What is the name of the file to read? '))
try:
    fhand = open(prompt)

except:
    print('Please choose an existing file')
    exit()
for line in fhand:
    #if line.startswith('From:'):
    line = line.upper()
    print(line)
