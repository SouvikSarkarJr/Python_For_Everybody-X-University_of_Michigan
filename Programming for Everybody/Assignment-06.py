
largest = None
smallest = None

while True:
    num = input('Enter Number : ')
    
    if num == 'done':
        break

    try:
        num = int(num)
    except ValueError:
        print('Invalid Output')
        continue

    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)