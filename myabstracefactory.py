class abstractfactory(object):
	def createProductA(self):
		pass
	def createProductB(self):
		pass
	
class concretefactory1(abstractfactory):
	def createProductA(self):
		pa = ProductA()
		pa.show()
	def createProductB(self):
		pb = ProductB()
		pb.show()
		
class ProductA(object):
	def __init__(self):
		pass
	def show(self):
		print("ProductA is created")
	
class ProductB(object):
	def __init__(self):
		pass
	def show(self):
		printf("ProductB is created")
	
def main():
	cf = concretefactory1()
	cf.createProductA()
	
if __name__ == "__main__":
	main()
	
