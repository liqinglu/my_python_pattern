class cls1(object):
	pass
	
class A(cls1):
	pass
	
class B(cls1):
	pass
	
class C(A,B):
	pass
	
class newaction(object):
	def visit(self,node,*args,**kw):
		meth = None
		for i in node.__class__.__mro__:
			meth_name = "visit_"+i.__name__
			meth = getattr(self,meth_name,None)
			if meth:
				break
		
		if not meth:
			meth =	self.generic_visit
		
		return meth(node,*args,**kw)
	def visit_C(self,node,*args,**kw):
		print "visit_C : %s"%node.__class__.__name__
	def visit_B(self,node,*args,**kw):
		print "visit_B : %s"%node.__class__.__name__
	def generic_visit(self,node,*args,**kw):
		print "generic_visit : %s"%node.__class__.__name__
	
cls = cls1()
a = A()
b = B()
c = C()
visitor = newaction()
visitor.visit(cls)
visitor.visit(a)
visitor.visit(b)
visitor.visit(c)
