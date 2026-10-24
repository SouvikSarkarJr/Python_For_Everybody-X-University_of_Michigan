
import re

handel_file = open ('/Users/souviksarkarjr./Documents/Python/Using Python to Access Web Data/data.txt')

numbers = re.findall(r'[0-9]+', handel_file.read())

total_sum = 0 

for num in numbers : 
    total_sum = total_sum + int(num)

print (total_sum)

handel_file.close()