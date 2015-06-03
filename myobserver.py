class subject(object):
	def __init__(self):
		self._observer = []
	def attach(self,o):
		if o not in self._observer:
			self._observer.append(o)
	def detach(self,o):
		try:
			self._observer.remove(o)
		except ValueError:
			pass
	def notify(self,modifier=None):
		for observer in self._observer:
			if modifier!=observer:
				observer.update(self)
   
class mydata(subject):
	def __init__(self,name=""):
		subject.__init__(self)
		self.name = name
		self._data = 0
	 
	@property
	def data1(self):
		return self._data
  
	@data1.setter
	def data1(self,v):
		self._data = v
		self.notify()
   
class hexviewer(object):
	def update(self,sub):
		print "hexviewer : %s is 0x%x"%(sub.name,sub.data1)
   
class decimalviewer(object):
	def update(self,sub):
		print "decimalviewer : %s is %d"%(sub.name,sub.data1)
   
def main():
	a = mydata("test1")
	b = mydata("test2")
	view1 = hexviewer()
	view2 = decimalviewer()
	a.attach(view1)
	a.attach(view2)
	b.attach(view1)
	b.attach(view2)
	
	a.data1 = 10
	b.data1 = 36
	
	a.detach(view1)
	b.detach(view2)
	
	a.data1 = 101
	b.data1 = 102
   
if __name__ == "__main__":
	main()