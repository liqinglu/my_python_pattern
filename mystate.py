class State(object):
	def __init__(self,state=0):
		self.state = state
		self.up = None
		self.down = None
		self.current = None
	
	def move(self,target):
		if self.state == target:
			print "Get %d floor, please go down"%target
		else:
			self.setcontext()
			if target > self.state:
				print "Get %d floor, up..."%self.state
				self.current = self.up
			else:
				print "Get %d floor, down..."%self.state
				self.current = self.down
			
			if self.current == None:
				print "error"
				return
			
			self.current.move(target)
			
	def setcontext(self):
		pass
		
class f1State(State):
	def __init__(self,state=1):
		super(f1State,self).__init__(state)
	
	def setcontext(self):
		self.up = f2State()
		self.down = None
	
class f2State(State):
	def __init__(self,state=2):
		super(f2State,self).__init__(state)
		
	def setcontext(self):
		self.up = f3State()
		self.down = f1State()
	
class f3State(State):
	def __init__(self,state=3):
		super(f3State,self).__init__(state)
	
	def setcontext(self):
		self.up = f4State()
		self.down = f2State()

class f4State(State):
	def __init__(self,state=4):
		super(f4State,self).__init__(state)
	
	def setcontext(self):
		self.up = None
		self.down = f3State()
		
class User(object):
	_state = State()
	
	def __init__(self,initial,name):
		self.name = name
		self._state = f1State()
		
	def goto(self,target):
		self._state.move(target)
	
def main():
	u = User(1,'user1')
	u.goto(4)
	
if __name__ == "__main__":
	main()