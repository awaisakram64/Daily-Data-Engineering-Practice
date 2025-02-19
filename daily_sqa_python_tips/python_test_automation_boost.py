import unittest

def test_login(user, password):
    if user == "tester" and password == "securePass":
        return True
    return False

class TestLoginFunction(unittest.TestCase):
    
    def test_valid_login(self):
        self.assertTrue(test_login("tester", "securePass"))
        
    def test_invalid_user(self):
        self.assertFalse(test_login("wrongUser", "securePass"))
        
    def test_invalid_password(self):
        self.assertFalse(test_login("tester", "wrongPass"))
        
if __name__ == '__main__':
    unittest.main()