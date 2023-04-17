import unittest

from .test_case import Test

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test))
    return test_suite

if __name__ == '__main__':
    my_suite = suite()
    runner = unittest.TextTestResult()
    result = runner.testsRun(my_suite)
