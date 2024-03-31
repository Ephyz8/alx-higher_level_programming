import urllib.request
"""Fetches https://alx-intranet.hbtn.io/status"""
url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
   try:
      with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("\t- Body response:")
        print("\t\t- type:", type(body))
        print("\t\t- content:", body)
   except urllib.error.URLError as e:
       print("Error fetching URL:", e)
       
