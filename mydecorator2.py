def hello(fn):
	def wrapper():
		print "before"
		print fn()
		print "after"
	return wrapper
	
@hello
def foo():
	print "hello, world"
	
foo()