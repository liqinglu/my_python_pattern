class Provider(object):
	def __init__(self):
		self.msgs = []
		self.subscribers = {}
		
	def notify(self,msg):
		self.msgs.append(msg)
		
	def subscribe(self,msg,who):
		self.subscribers.setdefault(msg,[]).append(who)
		
	def unsubscribe(self,msg,who):
		self.subscribers[msg].remove(who)
		
	def update(self):
		for inmsg in self.msgs:
			if inmsg in self.subscribers:
				for sublist in self.subscribers[inmsg]:
					sublist.info(inmsg)
	
class Subscriber(object):
	def __init__(self,name,provider):
		self.name = name
		self.provider = provider
		
	def subscribe(self,msg):
		self.provider.subscribe(msg,self)
		
	def info(self,msg):
		print("{} got {}".format(self.name,msg))
	
class Publisher(object):
	def __init__(self,msg_center):
		self.msg_center = msg_center
		
	def publish(self,msg):
		self.msg_center.notify(msg)
	
def main():
	provider = Provider()
	
	#publisher = Publisher(provider)
	
	wu = Subscriber('wu',provider)
	wu.subscribe('cartoon')
	san = Subscriber('san',provider)
	san.subscribe('movie')
	shu = Subscriber('shu',provider)
	shu.subscribe('music')
	
	provider.notify('cartoon')
	provider.notify('movie')
	provider.notify('music')
	provider.notify('gabage')
	provider.notify('sand')
	
	provider.update()
	
if __name__ == "__main__":
	main()