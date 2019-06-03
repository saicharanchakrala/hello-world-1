def hello():
	print("Hello World from Python")
	return

def greetings():
	name=input("Enter the name")
	print("Hello " +name+" from Python") 
	return

if __name__=='__main__':
	hello()
	greetings()
