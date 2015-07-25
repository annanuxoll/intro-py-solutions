# my first-draft solution to problem 1.3.2 

import math
import sys

def quad_solve(): 
	print "ax^2 + bx + c = 0"
	a = float(raw_input('What is a?'))
	b = float(raw_input('What is b?'))
	c = float(raw_input('What is c?'))

	disc1 = b**2 - (4*a*c)

	if a == 0:
		if b == 0 and c != 0: 
			print "Root is %r" % -c 
			sys.exit()
		elif b ==0 and c==0:
			print "Root is 0, dweeb"
			sys.exit()
		root = -c/b
		print "Put in a quadratic next time,"
		print "The intercept of that linear function is %s" % root
		sys.exit()

	if disc1 < 0: 
		print "Roots are imaginary!"
	else: 
		disc = math.sqrt(disc1)
		root1 = (-b + disc)/(2 * a)
		root2 = (-b - disc)/(2 * a)
		print "First root is %r"  %  root1
		print "Second root is %r"  %  root2

quad_solve()
