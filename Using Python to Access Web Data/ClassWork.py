
# ----------------------------------- Regular Expression ------------------------------------

# import re

# handel = open('/Users/souviksarkarjr./Documents/Python/Using Python to Access Web Data/mbox.txt')

# # for line in handel :
# #     if re.search('^From ',line):  # will show the lines starts with 'F'
# #         print (line)

# # for line in handel :
# #     if re.search ('^I.*#',line) : # will show the lines starts with 'I' and ends with '#'. Here '.*' represents any characters
# #         print (line)

# handel.close()



# x = 'My lucky number is : 5 or, 2'
# y = re.findall('[0-9]+',x)
# print (y)



# r = 'i used to love that girl very much, it was my fault that our vibe did not match'
# y = re.findall('[aeiou]+',r)

# count = 0 

# for i in y :
#     # print (y)
#     count = count + 1

# print (count) # 20


# p = 'I want to go to the bathroom; I am sure about that..'
# y = re.findall('I.+;',p)
# print (y) # I want to go to the bathroom;


# p = "I want to go to the bathroom; I am sure about that; I want to pee too..."
# y =re.findall('I.+?;',p) # this states that it's not greedy it's will find the nearest one and provide it as output
# print (y)


# k = 'Form : souviksarkarjr@gmail.com 12.00 pm 23rd Oct, 2026'
# y = re.findall('\S+@\S+',k)
# print (y)


# pos01 = k.find('@') <- this code is done below to execute using regular expression 
# print (pos01) # 21
# pos02 = k.find('.')
# print(pos02) # 27
# print(k[pos01 + 1 : pos02]) # gmail

# y = re.findall('@([^ ]*)',k)
# print (y)


# x = 'I have $100 in my savings account'
# y = re.findall('\$[0-9]+',x)
# print (y)


# ----------------------------------- Networks and Sockets ------------------------------------

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org' , 80))
#                 ^ Host          ^ Port



# ----------------------------------- Surf The Web ------------------------------------

# print (ord('H')) # prints asci code of 'H'

# x = u'Hola' # uni-code
# print(type(x))

# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# for line in fhand :
#     print(line.decode().strip())

# count = dict() 
# for line in fhand :
#     words = line.decode().split()
#     for word in words :
#         count[word] = count.get(word,0)+1
# print (count)

# Beautiful Soup (Need to Download the file named 'BS4' too)
# import urllib.request
# import urllib.parse
# import urllib.error
# from bs4 import BeautifulSoup

# url = input ('Enter - ')
# html = urllib.request.urlopen(url).read() 
# soup = BeautifulSoup(html,'html.parser')
# # retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags :
#     print (tag.get('href', None))



# ----------------------------------- Web Services ------------------------------------

# XML

# import xml.etree.ElementTree as ET
# data = '''<person>
#     <name> Souvik Sarkar Jr. </name>
#     <phone type='int'> 6291080287 </phone>
#     <email hide='yes'/> 
# </person>'''

# tree = ET.fromstring(data)
# print ('Name: ',tree.find('name').text)
# print ('Mobile Number: ',tree.find('phone').text)



# ----------------------------------- JSON ------------------------------------

import json 

# data = '''{
#     "name" :"Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+91 6291080287"
#     }, 
#     "email" : {
#         "hide" : "yes"
#     }
# }'''

# info = json.loads(data)
# print ('Name : ', info["name"])
# print ('Hide : ', info["email"]["hide"])



# input_data = """[
#     { 
#         "id": "001",
#         "x": "2",
#         "name": "Chuck" 
#     },
#     { 
#         "id": "009",
#         "x": "7",
#         "name": "Souvik"
#     } 
# ]"""

# info = json.loads(input_data)
# print("User Count :", len(info))

# for item in info:
#     print("Name :", item["name"])
#     print("Attributes :", item["x"])