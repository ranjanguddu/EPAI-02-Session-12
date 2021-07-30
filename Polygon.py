import math

class Polygon:
	'''this  is a polygon iterable class which takes radis and side leangth 
	2 parametersa and calculate few parameters on Polygon'''

	def __init__(self, n, r):
		'''to instantiate the class'''
		self.num_side = n
		self.radius = r
		self._interior_angle = None
		self._edge_length = None
		self._apothem = None
		self._area = None
		self._perimeter = None

	@property
	def radius(self):
		#print('getter method for radius gets  called')
		return self._radius

	@property
	def num_side(self):
		#print('getter method for num_side gets  called')
		return self._num_side

	@radius.setter
	def radius(self, rad):
		#print('setter method for radius gets  called')
		if isinstance(rad, int or float):
			if rad<0:
				raise ValueError('radius can''t be negative')
			else:
		
				self._radius = rad
				
		else:
			raise TypeError('Radius should be a number')
		
	
	@num_side.setter
	def num_side(self, num):
		#print('setter method for num_side gets  called')
		if isinstance(num, int):
			if num<3:
				raise ValueError('Minimum 3 vertices Polygon is possible')
			else:
		
				self._num_side = num
				
		else:
			raise TypeError('For a Ploygon, no of Vertices has to be a number')

		


		
	@property
	def edges(self):
		'''return no of edges '''
		return self.num_side

	@property
	def vertices(self):
		'''return no of vertices '''
		return self.num_side

	@property
	def interior_angle(self):
		'''calculate interior angle '''
		if self._interior_angle is None:
			print('calculating interior angle')
			self._interior_angle = (self.num_side-2)*180/self.num_side

		return self._interior_angle
		#return f'{(self.num_side-2)*180/self.num_side:.1f}'

	@property
	def edge_length(self):
		'''calculate edge length '''
		if self._edge_length is None:
			print('calculating edge length')
			self._edge_length = 2*self.radius*math.sin(math.pi/self.num_side)
		
		return self._edge_length
		#return f'{2*self.radius*math.sin(math.pi/self.num_side):.2f}'

	@property
	def apothem(self):
		'''calculate apothem '''
		if self._apothem is None:
			print('calculating apothem')
			self._apothem = self.radius*math.cos(math.pi/self.num_side)

		return self._apothem

		#return f'{self.radius*math.cos(math.pi/self.num_side):.2f}'

	@property
	def area(self):
		'''calculate area '''
		
		if self._area is None:
			print('calculating area')
			self._area = 0.5*self.num_side*float(self.apothem)*float(self.edge_length)

		return self._area
		#return f'{0.5*self.num_side*float(self.apothem)*float(self.edge_length):.2f}'
	
	@property
	def perimeter(self):
		'''calculate perimiter '''
		if self._perimeter is None:
			print('calculating perimeter')
			self._perimeter =  self.num_side*float(self.edge_length)

		return self._perimeter
		#return f'{self.num_side*float(self.edge_length):.2f}'

	def __eq__(self,other):
		''' implementing this method to copmare 2 polygomn  object'''
		if isinstance(other, Polygon):
			return self.num_side == other.num_side and self.radius == other.radius

		else:
			return "Can't compare different kind of object"
	
	def __gt__(self,other):
		'''to find if one polygon vertices no is greater than other or not'''
		if isinstance(other, Polygon):
			return self.num_side>other.num_side
		
			



	def __repr__(self):
		'''__rper__ method to give user an idea about the object creation'''
		#print(f'Calling Polygon __repr__ ')
		return f'Polygon:(num_side={self.num_side}, circumradius={self.radius}) created'





