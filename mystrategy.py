import types

class mystrategy(object):
	def __init__(self,func=None):
		self.name = "example 0"
		if func is not None:
			self.execute = types.MethodType(func,self)
		
	def execute(self):
		print self.name + " in class mystrategy"
	
def execute_rep1(self):
	print self.name + " in rep1"
	
def execute_rep2(self):
	print self.name + " in rep2"
	
def main():
	strat0 = mystrategy()
	strat1 = mystrategy(execute_rep1)
	strat1.name = "example 1"
	strat2 = mystrategy(execute_rep2)
	strat2.name = "example 2"
	
	strat0.execute()
	strat1.execute()
	strat2.execute()
	
if __name__ == "__main__":
	main()