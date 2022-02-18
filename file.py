class myphones:
	def __init__(self):
		self.x1 = "micro"
		print('this is my old phn...')
class redmi:
	def __init__(self):
		self.x2 = 'charger'
		print('this is the charger')
		super().__init__()
class nokia(redmi):redmi
	def __init__(self):
		self.x3 = 20,000;
		print('cost of my phn')
		super().__init__()
class vivo(nokia):
	def __init__(self):
		self.x4 = 60;
		print('hi....')
		super().__init__()
a = myphones()
a = 
print(a.x1)
print(a.x2)
print(a.x3)
print(a.x4)



