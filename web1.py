import urllib.request
fhand = urllib.request.urlopen('http://crummy.com')
for line in fhand:
    print(line.decode().strip())