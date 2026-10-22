
#-------------------------------------------    Strings     -------------------------------------------#

# str1 = 'Souvik'
# str2 = ' Sarkar'
# str3 = ' Jr.'

# str4 = str1 + str2 + str3

# print (str4) # Souvik Sarkar Jr.
# print (str1[1]) # o
# print (len(str4)) # including the spaces and the '.' in this case = 17

# count = 0
# for i in str1 :
#     print (count,':',i)
#     count = count + 1

# print (str4[0:8]) # will print index number 0 to index number 8 # this is called Slicing

# if 'a' in str4 :
#     print ('Yes Sir') 

# print (str4.lower()) # souvik sarkar jr.
# print (str4.upper()) # SOUVIK SARKAR JR.

# position = str4.find('Jr.')
# print (position)

# str5 = str4.replace('Souvik','Kabir')
# print (str5)

#-------------------------------------------    Files   -------------------------------------------#

# xfile = open ('Python/Unit-02/mbox.txt','r') # ('File Path', 'read/write operation's first alphabet')
# print (xfile)


# xfile = open('Python/Unit-02/mbox.txt')
# for content in xfile :
#     print (content)        # prints the content of the file


# xfile = open('Python/Unit-02/mbox.txt')
# count = 0
# for lines in xfile :
#     count = count + 1

# print (count) # number of lines are counted

# xfile = open('Python/Unit-02/mbox.txt')
# char = xfile.read() 
# print (len(char)) # number of characters


# xfile = open('/Users/souviksarkarjr./Documents/Python/Unit-02/mbox.txt')
# for line in xfile :
#     line = line.rstrip() # removes the un-necesarry blank spaces b/t lines
#     if line.startswith('My') :
#         print (line)

# ------------------------------------------------ Lists ------------------------------------------------

# friends = ['Souvik', 2004, 'Jr.'] # str, int, str
# # index ->     0       1       2
# print (list(range(len(friends))))

# for i in friends :
#     print (i)
#     print (type(i))

# print (friends[1]) # 2004

# lotto = [2, 4, 26, 41, 63]
# print (lotto) # 2 4 26 41 63
# lotto[4] = 2004
# print (lotto) # 2 4 26 41 2004

# greet = 'Hello Bob'
# print (len(greet)) # 9 -> includes the space b/t Hello and Bob

# list = [1, 'Souvik', 'Horen Da', 'Pok Pok', 9903210687]
# print (len(list)) # -> 5 only the number of members are counted 

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# # print (c) # 1 2 3 4 5 6
# # print (c[1:4]) # 2 3 4

# stuff = list() 
# stuff.append('book')
# stuff.append(2004)
# print (stuff) # book 2004

# numbers = [200, 60, 90, 80, 100]
# print (max(numbers)) # maximum numbers 
# print (min(numbers)) # minimum numbers
# print (sum(numbers)) # add all the elements
# print (sum(numbers)/len(numbers)) # average

# abc = 'With three words'
# stuff = abc.split() # split based on the "space"
# print (stuff)

# line = 'first; second; third'
# thing = line.split(';')
# print (thing)

# ------------------------------------------------ Dictionaries ------------------------------------------------

# cabinet = dict()

# cabinet['summar'] = 12
# cabinet['fall'] = 3
# cabinet['spring'] = 75

# print (cabinet)
# print(cabinet['fall'])

# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)
# ccc['cwen'] = ccc['cwen']+1
# print(ccc)

# counts = dict()
# names = ['Souvik', 'Sarkar', 'Tanika', 'Mou', 'Pompi', 'Tanika']
# for i in names : 
#     counts[i] = counts.get(i,0) + 1                                       # 0 is a default value
# print (counts)


# counts = dict()
# print ('Enter a line of text : ')
# line = input ('')

# words = line.split()

# print ('Words : ', words)

# print ('Counting...')

# for word in words :
#     counts[word] = counts.get(word,0)+1 
# print ('Counts',counts)

# counts = {'chuck' : 1 , 'feed' : 2, 'jan' : 100}

# for key in counts :
#     print (key, counts[key]) 

# print (list(counts)) # prints the 'characteristic' value
# print (counts.values()) # print the numeric valus 
# print (list(counts.items())) # print tuples

# for a,b in counts.items() : # a represents 
#     print (a,b)

# ------------------------------------------------ Tuples ------------------------------------------------

# (x,y) = (22,'Souvik')
# print (x)
# print (y)

# d = {'b':1, 'a':10, 'c':22}
# t = sorted(d.items(),reverse=True) # t = sorted(d.items())
# print(t)

# for a,b in t :
#     print (a,b)

# -------------------------------------------------------------------------------- Code -------------------------

# file_name = input ('Enter File Name : ')
# fh = open (file_name)
# counts = dict()

# for line in fh :
#     words = line.split()
#     for i in words :
#         counts[i] = counts.get(i,0) + 1

# # print (counts)

# max_word = None
# max_count = None

# for a,b in counts.items() :
#     if max_count is None or b > max_count :
#         max_word = a 
#         max_count = b

# print (max_word, max_count)

