class base(object):
	def __init__(self,args):
		self._successor = args
	def handler(self,request):
		i = self._handler(request)
		if not i:
			self._successor.handler(request)
	def _handler(self,request):
		raise NotImplementedError('Must provide implementation in subclass.')

class Base1(base):
	def _handler(self,request):
		if 0<=request<10:
			print "Base1 handle, request is {}".format(request)
			return True
	
class Base2(base):
	def _handler(self,request):
		if 10<=request<20:
			print "Base2 handle, request is {}".format(request)
			return True
	
class Base3(base):
	def _handler(self,request):
		if 20<=request<30:
			print "Base3 handle, request is {}".format(request)
			return True
	
class DefaultBase(base):
	def _handler(self,request):
		print "DefaultBase handle, request is {}".format(request) 
		return True
	
def main():
	o = Base1(Base2(Base3(DefaultBase(None))))
	requests = [1,3,9,37,48,22,11,19,103,8]
	for request in requests:
		o.handler(request)
		
	#print o
	#print o._successor
	#while(o is not None):
	#	print o.__class__.__name__
	#	o = o._successor
	
if __name__ == "__main__":
	main()