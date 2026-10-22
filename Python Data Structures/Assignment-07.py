
file_name = input ('Enter File Name : ')
fh = open (file_name)

hour_counts = dict() 

for line in fh :
    if not line.startswith('Form ') :
        continue 

    words = line.split()
    
    time_str = words[5]
    hour = time_str.split(":")[0]

    hour_counts[hour] = hour_counts.get(hour,0)+1

for hour, count in sorted(hour_counts.items()):
    print (hour, count)