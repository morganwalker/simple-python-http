# -*- coding: utf-8 -*-
import unittest
import main


class SimpleTest(unittest.TestCase):

    def test_fun_msg(self):
        self.assertTrue(main.get_fun_msg() in main.MSGS)

if __name__ == '__main__':
    unittest.main()
