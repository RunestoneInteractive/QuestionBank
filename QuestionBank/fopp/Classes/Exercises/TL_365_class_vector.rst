.. actex:: TL_365_class_vector
   :author: Tyler Luchko
   :difficulty: 1.3092369478
   :basecourse: fopp
   :chapter: Classes
   :subchapter: Exercises
   :topics: Classes/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0588235294
   :total_students_attempting: 51
   :num_students_correct: 20.0
   :mean_clicks_to_correct: 6.25

   Add ``dot_product()`` methods to the ``Vector``
   class below.  Don't worry about the case where the vector lengths
   don't match.
   
   Try using your completed class to calculate and print the results of
   
   .. math::
      (5.89, -1.00, 6.92, 8.32, 8.38, -5.56, 8.36)\cdot(-3.42, -3.7, 4.46, -7.33, 3.72, -8.30, -4.43)
      
   and
   
   .. math::
      (3.47, 3.23, 6.68)\cdot(-2.98, -9.27, 7.59)
      
   ~~~~
   class Vector:
   
       def __init__(self, coords):
           self.coords = coords[:]
   
       def add(self, vec):
           coords=[]
    for i in range(len(self.coords)):
        coords.append(self.coords[i] + vec.coords[i])
    return Vector(coords)
   
       def scalar_mult(self, scalar):
           coords=[]
    for i in range(len(self.coords)):
        coords.append(self.coords[i] * scalar)
    return Vector(coords)
   
       # Add your method here
   
   vec_a = Vector((5.89, -1.00, 6.92, 8.32, 8.38, -5.56, 8.36))
   vec_b = Vector([-3.42, -3.7, 4.46, -7.33, 3.72, -8.30, -4.43])
   vec_c = Vector((3.47, 3.23, 6.68))
   vec_d = Vector((-2.98, -9.27, 7.59))
   
   print(vec_a.add(vec_b).coords)
   print(vec_c.add(vec_d).coords)
   
   print(vec_a.scalar_mult(10).coords)
   
   print(vec_a.coords)
   
   
   ====
   from unittest.gui import TestCaseGui
   import math
   class myTests(TestCaseGui):
       def testOne(self):
      class _Vector:
          def __init__(self, coords):
       self.coords = coords
   def add(self, vec):
       return 8.99e9*self.q/( (self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2 )**0.5
      class _Vector:
   
                 def __init__(self, coords):
   	     self.coords = coords[:]
   
                 def add(self, vec):
       coords=[]
       for i in range(len(self.coords)):
           coords.append(self.coords[i] + vec.coords[i])
       return Vector(coords)
   
   def scalar_mult(self, scalar):
       coords=[]
       for i in range(len(self.coords)):
           coords.append(self.coords[i] * scalar)
       return Vector(coords)
   
   def dot_product(self, vec):
       result = 0
       for i in range(len(self.coords)):
           result += self.coords[i]* vec.coords[i]
       return result
       
   def cross_product(self, vec):
       return Vector([self.coords[1]* vec.coords[2] - self.coords[2]*vec.coords[1],
                 self.coords[2]* vec.coords[0] - self.coords[0]*vec.coords[2],
          self.coords[0]* vec.coords[1] - self.coords[1]*vec.coords[0]])
   
      def test_vector(coords_a, coords_b):
          vec_a = Vector(coords_a)
   vec_b = Vector(coords_b)
   _vec_a = _Vector(coords_a)
   _vec_b = _Vector(coords_b)
          self.assertAlmostEqual(vec_a.dot_product(vec_b), _vec_a.dot_product(_vec_b),
   7, 
          'Checking dot product of Vector({}) and Vector({})'.format(coords_a, coords_b))
      test_vector([3, 0 , -4], [1, 2, 3])
      test_vector( (5.89, -1.00, 6.92, 8.32, 8.38, -5.56, 8.36), (-3.42, -3.7, 4.46, -7.33, 3.72, -8.30, -4.43))
      test_vector( (3.47, 3.23, 6.68), (-2.98, -9.27, 7.59))
   myTests().main()