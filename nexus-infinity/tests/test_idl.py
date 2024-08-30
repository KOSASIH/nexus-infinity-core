import unittest
from idl import IDL

class TestIDL(unittest.TestCase):
    def setUp(self):
        self.idl = IDL()

    def test_parse(self):
        idl_code = "interface MyInterface { void myMethod(); };"
        self.idl.parse(idl_code)
        self.assertIsNotNone(self.idl.ast)

    def test_generate(self):
        idl_code = "interface MyInterface { void myMethod(); };"
        generated_code = self.idl.generate(idl_code)
        self.assertIsNotNone(generated_code)

if __name__ == "__main__":
    unittest.main()
