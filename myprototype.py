import copy

class AAA(object):
	def __init__(self):
		self.x = 3
		self.y = 8
		self.z = 15
		self.garbage = [88,77,66]
		
	def __str__(self):
		return '{} {} {} {}'.format(self.x,self.y,self.z,self.garbage)
	
class ProtoType(object):
	def __init__(self):
		self._objects = {}
		
	def subscribe(self,name,o):
		self._objects[name] = o
		
	def unsubscribe(self,name):
		del self._objects[name]
		
	def clone(self,name,**kw):
		obj = copy.deepcopy(self._objects[name])
		obj.__dict__.update(kw)
		return obj
	
def main():
	aaa = AAA()
	proto = ProtoType()
	proto.subscribe('aaa',aaa)
	bbb = proto.clone('aaa')
	ccc = proto.clone('aaa',x=1,y=2,z=3,garbage=[4,5])
	
	print([str(i) for i in (aaa,bbb,ccc)])
	
if __name__ == "__main__":
	main()