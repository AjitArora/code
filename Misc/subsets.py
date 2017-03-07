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

x(3)