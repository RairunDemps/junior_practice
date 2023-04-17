import unittest

# This is the class we want to test. So, we need to import it
from .person import Person

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    person = Person()
    user_id = []
    user_name = []

    def test_0_set_name(self):
        print("\nStart set_name test\n")
        for i in range(4):
            user_name = f"name {i}"
            user_id = self.person.set_name(user_name)
            self.user_id.append(user_id)
            self.user_name.append(user_name)
            self.assertIsNotNone(user_id)
        print(f"user_id length = {len(self.user_id)}\t", self.user_id)
        print(f"user_name length = {len(self.user_name)}\t", self.user_name)
        print("\nFinish set_name test\n")
    
    def test_1_get_name(self):
        print("\nStart get_name test\n")
        user_id_len = len(self.user_id)
        for i in range(6):
            if i < user_id_len:
                self.assertEqual(self.user_name[i], self.person.get_name(i))
            else:
                self.assertEqual("There is no such user", self.person.get_name(i))
        print("\nFinish get_name test\n")
