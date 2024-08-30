import unittest
from agi_core import AGICore

class TestAGICore(unittest.TestCase):
    def setUp(self):
        self.agi_core = AGICore()

    def test_init(self):
        self.assertIsInstance(self.agi_core, AGICore)

    def test_process_input(self):
        input_data = "Hello, world!"
        output = self.agi_core.process_input(input_data)
        self.assertIsNotNone(output)

    def test_generate_response(self):
        input_data = "What is your name?"
        response = self.agi_core.generate_response(input_data)
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
