
file_name = input ('Enter File Name : ')
fh = open(file_name)

list_01 = list()

for line in fh : 
    words = line.split()
    for word in words :
        if word not in list_01 :
            list_01.append(word)

list_01.sort()
print (list_01)