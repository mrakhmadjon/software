import unittest
from stringLen import stringLen

#print(stringLen("asaa"))

class TestInput(unittest.TestCase):
    def test_length(self):
        result = stringLen("something")
        self.assertEqual(result,len("somethign"))

    def test_length2(self):
        result = stringLen("laaa")
        self.assertEqual(result,1)


if __name__ == "__main__":
    unittest.main()
