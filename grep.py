import re
f = open('zen.txt', 'r')
content = f.read()

find_dutch = re.findall('Dutch', content)
print(find_dutch)

find_digits = re.findall('\d', content)
print(find_digits)

find_o = re.findall('.oo', content)
print(find_o)

f.close()