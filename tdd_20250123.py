import unittest
import sys
import statistics

def calculateStandardDeviation(numbers: list):
    #doing stuff
    result = 0
    return result

class TestCalc(unittest.TestCase):
    def testStandardDeviationPositiveInt(self):
        test_value = [3,4]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationNegativeInt(self):
        test_value = [-3,-4]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationPositiveFloat(self):
        test_value = [3.5,4.5]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationNegativeFloat(self):
        test_value = [-3.5,-4.5]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationMixed(self):
        test_value = [3,-4,3.5,-4.5]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationNull(self):
        test_value = None
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandandDeviationNotArray(self):
        test_value = 'pippo'
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationEmptyArray(self):
        test_value = []
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationArrayTooLarge(self):
        test_value = [] #like google of google of elements
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationNotNumbers(self):
        test_value = ['a', {}, False]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationNumbersTooBig(self):
        test_value = [sys.max_size, sys.max_size]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
    def testStandardDeviationNUmbersTooSmall(self):
        test_value = [sys.min_size, sys.min_size]
        self.assertEquals(calculateStandardDeviation(test_value), statistics.stdev(test_value), "not expected")
