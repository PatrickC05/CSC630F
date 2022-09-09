# Unit Testing

## Purpose
Unit testing allows developers to test individual parts, or "units" of code in isolation. Each unit's output is compared to its expected output, in hopes of creating a more efficient development cycle.

## Examples
1. In web apps, there are many parts to perform unit testing.
    1. The status page of a url can be tested to see if it is working.
    2. The content of a page can be tested to see if it is correct.
    3. Adding, editing, or removing data from a database can be tested.
2. Python has a built-in library called `unittest` that can be used to perform unit testing. Its official documentation includes the following example code: 

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```
The functions `assertEqual`, `assertTrue`, and `assertFalse` can be used to test if the output of a function is correct. Although used trivially in this example, these tests can be used to test more complex units such as the ones listed above.

## Defense of Unit Testing
Because unit testing evaluates each unit of code in isolation, bugs can be more easily detected. The developer will know which unit is at the source of the bug, saving time in the process. However, if only running a program from start to finish, an unexpected result could stem from anywhere. Even if the expected result is achieved, multiple mistakes could have canceled out. In large programs such as web apps, automated unit testing is also significantly more efficient than manually testing critical units, such as web pages or database queries. With just one set of tests, the developer can ensure that essential units are working properly. The automated nature of unit testing not only saves time in debugging code, but also reduces the time needed to test the code.

## Sources
https://www.geeksforgeeks.org/unit-testing-software-testing/

https://docs.djangoproject.com/en/4.1/topics/testing/overview/

https://docs.python.org/3/library/unittest.html