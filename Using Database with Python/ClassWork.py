
# ----------------------------------- Object Oriented Python -----------------------------------

# print (ord('H')) # 72
# print (ord('\n')) # 10

# letter = chr(108)
# print(letter)

# ----- Creating Object and Class

# class PartyAnimal:

#     def __init__(self):
#         self.x = 0

#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)

# an = PartyAnimal()

# an.party()
# an.party()
# an.party()

# # print ("Type", type(an))
# # print ("____________________")

# print ("Using Dir ", dir(an))

# # print ("____________________")
# # print ("Type", type(an.x))
# # print ("____________________")
# # print ("Type", type(an.party))
# # print ("____________________")

# ----- Destruction

# class PartyAnimal :
#     def __init__(self) :
#         self.x = 0
#         print ('I am constructed')
#     def party (self) :
#         self.x = self.x + 1 
#         print ('So Far',self.x)
#     def __del__(self) :
#         print ('I am destructed',self.x)
# an = PartyAnimal()
# an.party() 
# an.party()
# an = 42 
# print ('an contains', an)

# --- Inheritance

# class PartyAnimal:

#     def __init__(self, nam):
#         self.x = 0
#         self.name = nam
#         print(self.name, "constructed")

#     def party(self):
#         self.x = self.x + 1
#         print(self.name, "party count", self.x)


# class FootballFan(PartyAnimal):

#     def __init__(self, name):
#         super().__init__(name)
#         self.points = 0

#     def touchdown(self):
#         self.points = self.points + 7
#         self.party()
#         print(self.name, "points", self.points)


# s = PartyAnimal("Sally")
# s.party()

# j = FootballFan("Jim")
# j.party()
# j.touchdown()



# ----------------------------------- CLASS WORK -----------------------------------

# import sqlite3

# conn = sqlite3.connect('/Users/souviksarkarjr./Documents/Using_Database_with_Python/Email.db')
# cur = conn.coursor()

# cur.execute (''' 
# DROP THE TABLE IF EXISTS Counts ''')

# cur.execute ('''
# CREATE TABLE Counts (email TEXT, count INTEGER) ''')

# fname = input ('Enter File Name : ')
# if (len(fname)<1) : fname = 'mbox-short.txt'
# fh = open (fname)

# for line in fh :
#     if not line.startswith('From: ') : continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute ('Select count FROM Counts Where email = ?',(email,))

