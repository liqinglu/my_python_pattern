# -*- coding: utf-8 -*-

class A(object):
	def get(self):
		print "in A"

class B(object):
	def get(self):
		print "in B"

def factory(where):
	fact = dict(fromA=A,fromB=B)
	return fact[where]()
	
def main():
	a,b = factory("fromA"),factory("fromB")
	for i in range(4):
		if i%2:
			a.get()
		else:
			b.get()
	
if __name__ == "__main__":
	main()