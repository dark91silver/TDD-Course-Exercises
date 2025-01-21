#TDD esercizio 1
#nda: le funzioni di testing sono sotto solo per potere rendere il codice eseguibile
import unittest

#funzioni
class Calc():
    def sum(sum1, sum2):
        if not (type(sum1) == int or type(sum1) == float):
            raise Exception('sum1 must be a number')
        if not (type(sum2) == int or type(sum2) == float):
            raise Exception('sum2 must be a number')
        return sum1 + sum2
    def diff(minuendo, sottraendo):
        if not (type(minuendo) == int or type(minuendo) == float):
            raise Exception('minuendo must be a number')
        if not (type(sottraendo) == int or type(sottraendo) == float):
            raise Exception('sottraendo must be a number')
        return minuendo - sottraendo
    def mult(mul1, mul2):
        if not (type(mul1) == int or type(mul1) == float):
            raise Exception('mul1 must be a number')
        if not (type(mul2) == int or type(mul2) == float):
            raise Exception('mul2 must be a number')
        return mul1 * mul2
    def div(dividendo, divisore):
        if not (type(dividendo) == int or type(dividendo) == float):
            raise Exception('dividendo must be a number')
        if not (type(divisore) == int or type(divisore) == float):
            raise Exception('divisore must be a number')
        if divisore == 0 or divisore == 0.0:
            raise Exception('cannot divide by 0')
        return dividendo / divisore


#unit test
class TestCalc(unittest.TestCase):
    def testSumOk(self):
        testValue = 8
        result = Calc.sum(6,2)
        self.assertEqual(testValue, result, "I was expecting 8")
        print(f'I got the correct sum: {testValue} = {result}')
    def testDiffOk(self):
        testValue = 4
        result = Calc.diff(6,2)
        self.assertEqual(testValue, result, "I was expecting 4")
        print(f'I got the correct diff: {testValue} = {result}')
    def testMultOk(self):
        testValue = 12
        result = Calc.mult(6,2)
        self.assertEqual(testValue, result, "I was expecting 12")
        print(f'I got the correct mult: {testValue} = {result}')
    def testDivOk(self):
        testValue = 3
        result = Calc.div(6,2)
        self.assertEqual(testValue, result, "I was expecting 3")
        print(f'I got the correct div: {testValue} = {result}')

if __name__ == '__main__':
    unittest.main()
