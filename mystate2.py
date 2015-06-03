import types
import time

INITIALFLOOR = 1

class State(object):
	def __init__(self):
		pass
		
	def pick(self,target,context):
		if self.state == target:
			print "Pick up a person at %d floor"%target
			return
		else:
			if self.state > target:
				print "down,Now is %d floor"%self.state
				context.current = context._state_list[self.state-2]
				time.sleep(1)
				context.current.pick(target,context)
			else:
				print "up, Now is %d floor"%self.state
				context.current = context._state_list[self.state]
				time.sleep(1)
				context.current.pick(target,context)
				
	def go(self,target,context):
		#print self.__class__.__name__
		#print self.__dict__
		if self.state == target:
			print "Get %d floor"%target
			return
		else:
			if self.state > target:
				print "down,Now is %d floor"%self.state
				context.current = context._state_list[self.state-2]
				time.sleep(1)
				context.current.go(target,context)
			else:
				print "up, Now is %d floor"%self.state
				context.current = context._state_list[self.state]
				time.sleep(1)
				context.current.go(target,context)

class f1State(State):
	def __init__(self,state=1):
		super(f1State,self).__init__()
		self.state = state
	
class f2State(State):
	def __init__(self,state=2):
		super(f2State,self).__init__()
		self.state = state
	
class f3State(State):
	def __init__(self,state=3):
		super(f3State,self).__init__()
		self.state = state
	
class f4State(State):
	def __init__(self,state=4):
		super(f4State,self).__init__()
		self.state = state
	
class Context(object):
	subcontext = [f1State,f2State,f3State,f4State]
	_state_list = []
	current = None
	def __init__(self):
		for i in Context.subcontext:
			Context._state_list.append(i())
			
		if self.current == None:
			self.current = Context._state_list[INITIALFLOOR-1]
			
		self.userat = 0
			
	def _display(self):
		for lst in self._state_list:
			print lst.__dict__
			
	def request(self,target):
		self.current.go(target,self)
		
	def setfloor(self,floor):
		self.current.pick(floor,self)

def main():
	context = Context()
	#context._display()
	
	#context.setfloor(1)
	context.request(2)
	print
	#context.setfloor(2)
	context.request(4)
	print
	#context.setfloor(3)
	context.request(1)
	
if __name__ == "__main__":
	main()