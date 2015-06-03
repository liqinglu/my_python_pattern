def makeHtmlTag(tag,*args,**kwds):
	def real_decorator(fn):
		css_class = " class='{0}'".format(kwds["css_class"]) \
		                                       if "css_class" in kwds else ""
		#def wrapped(*args,**kwds):
		#	return "<"+tag+css_class+">" + fn() + "</"+tag+">"
		#return wrapped
		#outputstr = "<"+tag+css_class+">" + fn() + "</"+tag+">"
		def wrapper():
			outputstr = "<{} {}>{}</{}>".format(tag,css_class,fn(),tag)
			return outputstr
		return wrapper
	return real_decorator

@makeHtmlTag(tag="b",css_class="bold_css")
@makeHtmlTag(tag="i",css_class="italic_css")
def hello():
	return "hello world"
	
#hello = makeHtmlTag(tag,*args,**kwds)(hello)
print hello()