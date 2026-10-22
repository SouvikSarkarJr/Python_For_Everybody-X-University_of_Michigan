file_name = input('Enter File Name : ')

try : 
    xfile = open(file_name, 'r')
except :
    print ('Invalid File Name')
    quit()


for content in xfile :
    print (content.strip().upper())