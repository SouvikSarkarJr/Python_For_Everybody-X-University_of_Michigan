import json
import ssl
import urllib.parse
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Base API URL
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# 1. Prompt user for location
address = input("Enter location: ")
if len(address) < 1:
    address = "Sharif University of Technology"

# 2. Encode parameters and construct target URL
parms = dict()
parms["q"] = address.strip()
url = serviceurl + urllib.parse.urlencode(parms)

print(f"Retrieving {url}")

# 3. Fetch data from web service
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print(f"Retrieved {len(data)} characters")

# 4. Parse JSON
try:
    js = json.loads(data)
except Exception:
    js = None

if not js or "features" not in js:
    print("==== Failure To Retrieve ====")
    print(data)
    exit()

# 5. Extract and print the first plus_code
plus_code = js["features"][0]["properties"]["plus_code"]
print(f"Plus code {plus_code}")
