import unittest 
from robot import Robot

class testRobot(unittest.TestCase):
    
    def setUp(self): # this block runs before every test
        self.mega_man = Robot("Mega Man",battery = 50)

    def test_battery(self):
        
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery,100)

    def test_say_name(self):
        
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOP! I am Mega Man")
        self.assertEqual(self.mega_man.battery,49)
        

if __name__ == '__main__':
    unittest.main() 