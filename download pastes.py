import os
import requests

if os.path.isdir('.//downloads//'):
    pass
else:
    os.mkdir('.//downloads//')

with open('links.txt') as handle:
    lines = handle.readlines()
    for line in lines:
        code = line[21:].rstrip()
        filename = code + ".txt"
        fileloc = './/downloads//'+filename
        url = 'https://pastebin.com/raw/' + code
        print ("Downloading: " + filename + " From: " + url)
        r = requests.get(url, allow_redirects=True)
        try:
            open(fileloc, 'wb').write(r.content)
        except Exception:
            pass
