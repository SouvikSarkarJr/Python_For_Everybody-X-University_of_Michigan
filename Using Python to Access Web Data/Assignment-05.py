import json
import urllib.request
import ssl

# Ignore SSL certificate errors (useful for some environments/operating systems)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 1. Prompt for URL
url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_2484224.json"

print(f"Retrieving {url}")

# 2. Open the URL and read the response
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print(f"Retrieved {len(data)} characters")

# 3. Parse JSON data into Python dictionaries/lists
info = json.loads(data)

# 4. Extract comments and calculate total sum
comments = info["comments"]
total_sum = 0
count = 0

for item in comments:
    total_sum += int(item["count"])
    count += 1

print(f"Count: {count}")
print(f"Sum: {total_sum}")
