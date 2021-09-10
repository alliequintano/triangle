import unittest

# Function: triangle
#
#  Given the lengths of three sides of a triangle, classify it 
#  by returning one of the following strings:
#
#   "equ" - The triangle is equilateral, i.e. all sides are equal
#   "iso" - The triangle is isoscelese, i.e. only two sides are equal
#   "sca" - The triangle is scalene, i.e. no sides are equal
#   "err" - The arguments do not describe a valid triangle
#
def triangle(a, b, c):
    for item in a, b, c:
        if not isinstance(item, int) and not isinstance(item, float):
            return "err"
        if (item <= 0):
            return "err"
    
    listOfSides = sorted([a, b, c])
    if (listOfSides.pop() > sum(listOfSides)):
        return "err"
    if (a == b and b == c):
        return "equ"
    if (a == b or a == c or b == c):
        return "iso"
    return "sca"


class Tests(unittest.TestCase):
    
    def testTriangle(self):
        self.assertEqual('equ', triangle(1, 1, 1))
        self.assertEqual('iso', triangle(1, 1, 2))
        self.assertEqual('iso', triangle(1, 2, 2))
        self.assertEqual('sca', triangle(1, 2, 3))
        self.assertEqual('err', triangle(1, 1, "x"))
        self.assertEqual('err', triangle(1, -1, 1))
        self.assertEqual('iso', triangle(1/6, 1, 1))
        self.assertEqual('sca', triangle(1, 1.5, 2))
        self.assertEqual('err', triangle(1, 2, 4))
      # handle zero length

unittest.main()
