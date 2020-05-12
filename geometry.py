'''
GEOMETRY MODULE: Plane Geometry 
'''

'''
This module handles calculation on plane geometry shapes. This includes:
	
1. Circle : A circle can be defined as the locus of all points equidistant from a central point

2. Triangle: A triangle can be defined as  “A two dimensional plane figure with three straight sides and three angles”.

3. Quadrilateral: A Quadrilaterals is defined as a simple closed figure bounded by four lines in plane. Types of Quadrilateral includes:
	
	1. Rectangle: is aparallelogram having any one of its angle as right angle ( 90°).
	2. Square:
	3. Trapezium: is a quadrilateral having one pair of opposite sides parallel to each other.
	4. Parallelogram : is a quadrilateral that has opposite sides parallel.
	
'''

from math import *


#CIRCLES
class Circle():
	'''Creates class objects'''
	def __init__(self, radius, angle= None, height = None):
		self.radius = radius
		self.angle = angle
		self.height = height
		
	def area(self):
		'''Calculates the area of a class'''
		return pi * (self.radius**2)
		
	def circumference(self):
		'''Calculates the circumference of a circle'''
		return 2 * pi * self.radius
	
	def arc_length(self):
		'''Calculates the length of Arc of a circle'''
		return (self.angle * pi * self.radius) / 180
	
	def sector_area(self):
		'''Calculates the area of a sector in a circle'''
		return (self.angle/360) * pi * (self.radius ** 2)
	def segment_area(self):
		'''Calculates the area of a segment in a circle'''
		return self.sector_area() - ((1/2)*sin(self.angle)*(self.radius**2))
		
	def segment_perimeter(self):
		'''Calculates the perimeter of a segment in. circle'''
		return self.arc_length() + (2 * self.radius * sin(self.angle/2))
	
	def chord_length(self):
		'''Calculates the length of chord in a circle'''
		return 2 * sqrt(self.height * ((2*self.radius) - self.height))

				
#TRIANGLES
class Triangle():
	def __init__(self, base, side1 = None, side2 = None, height = None, type = None):
		self.base = base
		self.side1 = side1
		self.side2 = side2
		self.height = height
		self.type = type
		
	def perimeter(self):
		return self.base + self.side1 + self.side2
	
	def area(self, type=None):
		
		if self.type == "sides":
			s = (self.base + self.side1 + self.side2)/2
			return sqrt(s * (s - self.base) * (s - self.side1) * (s - self.side2))
			
		elif self.type == "height":
			return (1/2) * self.base * self.height

class Equilateral(Triangle):
	def perimeter(self):
		return self.base * 3
	
	def area(self):
		return (sqrt(3/4)) * (self.base**2)
	


#QUADRILATERALS
class __Quadrilateral():
	def __init__(self, base, base2 = None, height = None, diagonal = None):
		self.base = base
		self.height = height
		self.diagonal= diagonal
		self.base2 = base2
	
class Rectangle(__Quadrilateral):
	def area(self):
		return self.base * self.height
	
	def perimeter(self):
		return 2 * (self.base + self.height)
		
	def diagonal_len(self):
		return sqrt((self.base ** 2) + (self.height ** 2))
	
class Square(__Quadrilateral):
	def area(self):
		return self.base ** 2
		
	def perimeter(self):
		return 4 * self.base
	
	def diagonal_len(self):
		return sqrt(2) * self.base
		
class Trapezium(__Quadrilateral):
	def area(self):
		return (1/2) * (self.base + self.base2 )* self.height
		
class Parallelogram(__Quadrilateral):
	def area (self):
		return self.base * self.height
		
	def perimeter(self):
		return 2 * (self.base + self.diagonal)		