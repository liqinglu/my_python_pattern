class MyProduct(object):
	product_info = {
		"orange":{'price':1,'quantity':10},
		"apple":{'price':2.02,'quantity':100},
		"pineapple":{'price':6.97,'quantity':39},
		"grape":{'price':3.88,'quantity':23}
	}
	
class MyView(object):
	def product_list(self,list):
		print "PRODUCT_LIST:"
		for i in list:
			print i
			
	def product_info(self,name,info):
		print "PRODUCT_INFO:"
		print "we have %s : price=%.2f , quantity=%d"%(name,info.get('price',0),info.get('quantity',0))
		
	def non_product_info(self,name):
		print "PRODUCT_INFO:"
		print "we do not have %s"%name
	
class MyController(object):
	def __init__(self):
		self.view = MyView()
		self.product = MyProduct()
		
	def product_list(self):
		list = self.product.product_info.keys()
		self.view.product_list(list)
		
	def product_info(self,name):
		try:
			myinfo = self.product.product_info.get(name,None)
			self.view.product_info(name,myinfo)
		except AttributeError,e:
			self.view.non_product_info(name)
	
def main():
	controller = MyController()
	controller.product_list()
	controller.product_info('orange')
	controller.product_info('pea')
	
if __name__ == "__main__":
	main()