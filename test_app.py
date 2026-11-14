import uniittest
from app import greet
class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello Devops")