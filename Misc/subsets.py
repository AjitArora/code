def x(s):
 j = pow(2, s)
 for i in xrange(0, j):
  l = 1
  for k in xrange(0, s):
   if i&l:
    print "1",
   else:
    print '0',
   l*=2
  print ""

# 'abc' > ["abc", "abC", "aBc", "Abc", "ABc", "AbC", "aBC", "ABC"]
def func(str):
 ret = []
 j = pow(2, len(str))
 for i in xrange(0, j):
  l = 1
  s = ""
  for k in xrange(0, len(str)):
   if i&l:
    s += str[k].upper()
   else:
    s += str[k].lower()
   l*=2
  ret.append(s)
 return ret

def func1(str):
 ret = set()
 j = pow(2, len(str))
 for i in xrange(0, j):
  l = 1
  s = ""
  for k in xrange(0, len(str)):
   if i&l:
    s += str[k].upper()
   else:
    s += str[k].lower()
   l*=2
  ret.add(s)
 return list(ret)

# '0ab' > ["0ab", "0aB", "0Ab", "0AB"]

print func1('abc')
print func1('abc0')