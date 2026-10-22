#-------------------------------------------------------------------------------#
#-------------------------------- Basic-----------------------------------------#
#-------------------------------------------------------------------------------#

print ("Hello World")

# i = 9903210687
# print (type(i))

# name = input('Who are you ? ')
# print ('Wolcome', name)

# print ("123" + "abc")

# x = int(98.6)
# print(x)

# x = int(input('Enter Number :'))
# if x % 2 == 0 :
#   print('Even')
# if x % 2 != 0 :
#  print('Odd')

# x = int(input('Enter Number :'))
# if x % 2 == 0 :
#   print('Even')
# elif x % 2 != 0 :
#  print('Odd')
# else:
#   print('Fuck You')

# x = int(input('Enter Your Size : '))
# if x==4 :
#     print ("It's Medium")
# elif x<4 :
#     print ("It's Small")
# else :
#     print ('Respect Sir !!!!') 


#-------------------------------------------------------------------------------#
#---------------------- Try and Escept Condition -------------------------------#
#-------------------------------------------------------------------------------#

# x = 'Hello Bob !!!'

# try : 
#     x = int(x)
# except :
#     x = -1

# print ('First',x)

# x = '123'

# try :
#     x = int(x)
# except :
#     x = -1

# print ('Second',x)


#-------------------------------------------------------------------------------#
#-----------------------------Functions-----------------------------------------#
#-------------------------------------------------------------------------------#

# def thing () :
#     print ('Hello')
#     print ('Mr. Souvik')

# thing () # 1 call
# print ('Fuck You')
# thing () # 2 call

# 1st

# def greet (lan) :
#     if lan == 'english' :
#         print ('Hello')
#     if lan == 'hindi' :
#         print ('Namaste')
#     if lan == 'bhojpuri' :
#         print ('Bhabi Ka Dhori Chat Lo')

# x = str(input('Enter Your Language : '))
# greet(x)

# 2nd 

# def greet () :
#     return 'Hello'

# print ('Souvik',greet())

# Combiniton of 1 and 2 

# def greet (lan) :
#     if lan == 'english' :
#         return 'Hello'
#     if lan == 'hindi' :
#         return 'Namaste'

# x = str ( input ('Enter Language : ') )
# print (greet(x),'Souvik')

# add 2 numbers 

# def add (a, b) :
#     return a+b 

# print(add(3,2))

# x = 'banana'
# y = max(x) # takes the string's highest value alphabet
# print(y)


#-------------------------------------------------------------------------------#
#-------------------------------Loops-------------------------------------------#
#-------------------------------------------------------------------------------#

# x = 5 
# while x>0 :
#     print (x)
#     x = x-1

# print ('Bla Bla Bla')
# print (x)


# for i in [5, 4, 3, 2, 1] :
#     print (i)

# friends = ['Bramha Dev', 'Vishnu Dev', 'Mahadev Sivh', 'Shakti Maa']
# for i in friends :
#     print ('Happy New Year : ',i)



# finding the largest number ----------------------------------------------

# largest_number = -1

# print ('Before',largest_number)

# array = [9, 80, 77, 68, 51, 49, 32, 20, 11]

# for i in array :
#     if i > largest_number :
#         largest_number = i

# print ('After',largest_number)


# finding the largest number ----------------------------------------------

# smallest_number = None

# array = [91, 90, 15, 61, 20, 1]

# for i in array :
#     if smallest_number is None :
#         smallest_number = i
#     elif i < smallest_number :
#         smallest_number = i

# print (smallest_number)


# count inside loop ---------------------------------------------------------

# i = 1 
# name_list = ['Souvik', 'Sarkar', 'Junior']
# for name in name_list :
#     print (i,name)
#     i = i+1



# sum inside loop -----------------------------------------------------------

# sum = 0
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in number_list :
#     sum = sum + number

# print (sum)


# Finding Avg. ------------------------------------------

# sum = 0
# count = 0

# number_list = [9,8,7,6,5,4,3,2,1] 

# for number in number_list :
#     count = count + 1
#     sum = sum + number


# # print (count) # 9
# # print (sum) # 45

# average = sum / count

# print (average)

