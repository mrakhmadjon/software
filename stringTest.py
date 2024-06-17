import unittest
from strlng import strlng

print(strlng("asaa"))

class TestInput(unittest.TestCase):
    def test_length(self):
        result = strlng("something")
        self.assertEqual(result,len("somethign"))

    def test_length2(self):
        result = strlng("laaa")
        self.assertEqual(result,1)


if(__name__) == '_main_':
    unittest.main


