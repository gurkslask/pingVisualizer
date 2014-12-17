import unittest
import pingVisualizer

class test_pingVisualizer(unittest.TestCase):
    def setUp(self):
        pass

    def test_ping(self):
        pingTime = pingVisualizer.getPingTime()
        print('Tid {}'.format(pingTime))
        self.assertLess(pingTime, 50)
        self.assertEqual(float, type(pingTime))

if __name__ == '__main__':
    unittest.main()