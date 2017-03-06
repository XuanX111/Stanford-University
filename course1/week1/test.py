import math

class karatsuba:

	def _init__(self):
		print "Karatsuba online!"

	def multiply(self, x, y):
		sx = str(x)
		sy = str(y)
		nx = len(sx)
		ny = len(sy)
		if nx==1 or ny==1:
			r = int(x)*int(y)
			return r
		n = nx
		if nx>ny:
			sy = sy.rjust(nx, '0')
			n = nx
		elif ny>nx:
			sx = sx.rjust(ny, '0')
			n = ny
		m = n % 2
		offset = 0
		even = n
		if m!=0:
			n+=1
			offset = 1
		floor = int(math.floor(n/2))-offset
		ceil = int(math.ceil(n/2))-offset
		a = sx[0:floor]
		b = sx[ceil:n]
		c = sy[0:floor]
		d = sy[ceil:n]
		r = ((10**n)*self.multiply(a,c)) + ((10**(n/2))*(self.multiply(a,d) + self.multiply(b,c))) + self.multiply(b,d)
		return r


k = karatsuba();
print k.multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
print 3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627
