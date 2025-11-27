import unittest
from main import ComplexNumber, find_largest_magnitude

class TestComplexNumber(unittest.TestCase):
    
    def test_basic(self):
        # Проверяем, что числа создаются правильно
        num = ComplexNumber(3, 4)
        self.assertEqual(num.real, 3)
        self.assertEqual(num.imaginary, 4)
    
    def test_show(self):
        # Проверяем, как числа показываются на экране
        self.assertEqual(str(ComplexNumber(3, 4)), "3 + 4i")
        self.assertEqual(str(ComplexNumber(3, -4)), "3 - 4i")
        self.assertEqual(str(ComplexNumber(3, 0)), "3 + 0i")
    
    def test_math(self):
        # Проверяем сложение, вычитание, умножение и модуль
        a = ComplexNumber(3, 4)
        b = ComplexNumber(1, -2)
        
        c = a + b
        self.assertEqual(c.real, 4)
        self.assertEqual(c.imaginary, 2)
        
        d = a - b
        self.assertEqual(d.real, 2)
        self.assertEqual(d.imaginary, 6)
        
        e = a * b
        self.assertEqual(e.real, 11)
        self.assertEqual(e.imaginary, -2)
        
        self.assertAlmostEqual(a.magnitude(), 5.0)
    
    def test_errors(self):
        # Проверяем, что с текстом работать нельзя
        num = ComplexNumber(3, 4)
        with self.assertRaises(TypeError):
            num + "text"
        with self.assertRaises(TypeError):
            num - "text"
        with self.assertRaises(TypeError):
            num * "text"

class TestFindLargest(unittest.TestCase):
    
    def test_find(self):
        # Ищем число с самым большим модулем
        nums = [ComplexNumber(3, 4), ComplexNumber(6, 8), ComplexNumber(1, 1)]
        result = find_largest_magnitude(nums)
        self.assertEqual(result.real, 6)
        self.assertEqual(result.imaginary, 8)
    
    def test_special_cases(self):
        # Проверяем пустой список и список с одним числом
        self.assertIsNone(find_largest_magnitude([]))
        
        single = [ComplexNumber(3, 4)]
        result = find_largest_magnitude(single)
        self.assertEqual(result.real, 3)

if __name__ == '__main__':
    unittest.main()