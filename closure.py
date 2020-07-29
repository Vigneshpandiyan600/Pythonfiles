import logging 
# this line creates a log file names example.log
logging.basicConfig(filename=r'example.log', level=logging.INFO)

def log(func):

	function = func
	def inner_log(*args):
		logging.info(f'arguments {args} called for function {function.__name__}')
		print(function(*args))
	return inner_log

@log
def add(x,y):
	return x+y
def sub(x,y):
	return x-y
add(10,5)
# my_fun = log(add)
# my_fun(3,4)
