class abstractsub(object):
	def __init__(self):
		pass
		
	def request(self):
		pass
	
class realsub(object):
	def __init__(self):
		pass
		
	def request(self):
		print "I am real subject"
	
class proxysub(object):
	def __init__(self):
		self._rs = None
		
	def request(self):
		self._rs = realsub()
		self.before()
		self._rs.request()
		self.after()
		
	def before(self):
		print "ready"
	def after(self):
		print "end"
	
def main():
	proxy = proxysub()
	proxy.request()
	
if __name__ == "__main__":
	main()