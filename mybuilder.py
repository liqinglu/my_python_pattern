class Director(object):
	def __init__(self):
		self.worker = None
	def buildcar(self):
		self.worker.newcar()
		self.worker.newcircle()
		self.worker.newbody()
	def getcar(self):
		return self.worker.car
	
class Worker(object):
	def __init__(self):
		self.car = None
	def newcar(self):
		self.car = Car()
		
class AudiWorker(Worker):
	def newcircle(self):
		self.car.circle = "Goodyear"
	def newbody(self):
		self.car.body = "Audi"
	
class BMWWorker(Worker):
	def newcircle(self):
		self.car.circle = "BridgeStone"
	def newbody(self):
		self.car.body = "BMW"	
	
class Car(object):
	def __init__(self):
		self.circle = None
		self.body = None
	def __repr__(self):
		return "Car body is {0.body}, wheel is {0.circle}".format(self)
	
def main():
	director = Director()
	director.worker = AudiWorker()
	director.buildcar()
	car = director.getcar()
	print(car)
	
if __name__ == "__main__":
	main()