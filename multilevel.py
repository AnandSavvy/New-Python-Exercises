class myphones:
	def __init__(self):
		self.x1 = "micro"
		print('this is my old phn...')
class redmi:
	def __init__(self):
		self.x2 = 'charger'
		print('this is the charger')
		super().__init__()
class nokia(redmi):
	def __init__(self):
		self.x3 = 20,000;
		print('cost of my phn')
		super().__init__()
class vivo(nokia):  # 
	def __init__(self):
		self.x4 = 60;  # assining valye to the variable 
		print('hi....')
		super().__init__()
a = myphones() # creating an object for instance variable 
print(a.x1)
r = redmi()
print(r.x2)
n = nokia()
print(n.x3)
v = vivo()
print(v.x4)




