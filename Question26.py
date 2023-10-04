import unittest

def name():
    name = 'MIGUEL'
    return name

class myTest(unittest.TestCase):

    def test(self):
        self.assertEqual(name(), 'JOHNRAE')

if __name__=='__main__':

    unittest.main()   