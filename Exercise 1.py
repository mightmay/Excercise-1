# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 01:22:31 2019
"""
import math
class Circle:
  def __init__(self, radius):
    self.radius = radius


  def computeArea(self):
    self.area = math.pi*math.pow(self.radius,2) 
    print("Area is " + str(self.area))

  def computePerimeter(self):
    self.perimeter = 2 * math.pi * self.radius
    print("Perimeter is " + str(self.perimeter))
    
c1= Circle(2)
c1.computeArea()
c1.computePerimeter()