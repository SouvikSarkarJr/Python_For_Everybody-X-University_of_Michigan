file_name = input("Enter File Name : ")

fh = open(file_name)

counts = dict()

# Building the histogram of sender email addresses

for line in fh:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender, 0) + 1

# Maximum loop to find the most prolific committer
max_email = None
max_count = None

for email, count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(max_email, max_count)
