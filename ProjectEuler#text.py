import urllib.request

data = urllib.request.urlopen('https://projecteuler.net/project/resources/p022_names.txt')
new_names = data.read()
new_names = new_names.title()
with open('final_names.txt', 'wb') as final:
    final.write(new_names)
print(final)