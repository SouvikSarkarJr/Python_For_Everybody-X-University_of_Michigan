
file_name = input('Enter File Name : ')
xfile = open(file_name)

total = 0 
count = 0 

for line in xfile : 
    if not line.startswith('X-DSPAM-Confidence:') :
        continue

    colon_position = line.find(':') # finding colon
    number = float(line[colon_position+1:])

    total = total + number 
    count = count + 1

average = total / count 

print("Average spam confidence:", average)