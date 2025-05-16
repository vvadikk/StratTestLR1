s = 'Pyth1abch2hon'
first = s.find('h')
last = s.rfind('h')
mid = s[first + 1:last]
s = s[:first + 1] + mid[::-1] + s[last:]
print(s)