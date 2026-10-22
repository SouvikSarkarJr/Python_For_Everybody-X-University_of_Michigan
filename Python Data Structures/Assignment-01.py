text = "X-DSPAM-Confidence:0.8475"

index_number_of_colon = text.find(':')

# print (index_number_of_colon) # 18

number = float(text[index_number_of_colon+1:]) # converted in float 

print (float(number))

# print(type (number)) # float