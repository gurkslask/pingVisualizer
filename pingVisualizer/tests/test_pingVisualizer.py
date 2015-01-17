#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pingVisualizer
----------------------------------

Tests for `pingVisualizer` module.
"""

import unittest

from pingVisualizer import pingVisualizer


class TestPingvisualizer(unittest.TestCase):

    def setUp(self):
        pass

    def test_ping(self):
        pv = pingVisualizer.pingVisualizer({'adress': '127.0.0.1'})
        pingTime = pv.getPingTime()
        print('Tid {}'.format(pingTime))
        self.assertLess(pingTime, 50)
        self.assertEqual(float, type(pingTime))

if __name__ == '__main__':
    unittest.main()
