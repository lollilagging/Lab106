import code
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    self.assertEqual(code.return_zero(),0)

  def testdouble(self):
    self.assertEqual(code.double(2), 2*2)
    self.assertEqual(code.double(4), 4*2)
    self.assertEqual(code.double(0), 0*2)
    self.assertEqual(code.double(-2), 4)
    
if __name__=='__main__':
  unittest.main()