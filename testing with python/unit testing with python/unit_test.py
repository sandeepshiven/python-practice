import unittest
from activity import eat,nap,is_funny,laugh

class ActivityTests(unittest.TestCase):

    def test_eat_healthy(self):
        """ Eating healthy to maitain body"""
        self.assertEqual(eat("broccoli",isHealthy = True),
        "I'm eating broccoli, because my body is a temple"
        )

    def test_eat_unhealthy(self):
        """ Unhealthy eating is not good """
        self.assertEqual(
            eat('pizza',isHealthy=False),
            "I'm eating pizza, because YOLO!"
            )   
    
    def test_eat_healthy_boolean(self):
        with self.assertRaises(ValueError):
            eat("pizza",isHealthy='who cares?')

    def test_short_nap(self):
        """ Short nap refreshes """
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed"
        )
    
    def test_long_nap(self):
        """ Long naps aren't good """
        self.assertEqual(
            nap(2),
            "Ugh I overslept"
        )
    
    def test_is_funny_tim(self):
        #self.assertEqual(is_funny('tim'),False)
        self.assertFalse(is_funny('tim'), 'tim should not be funny')

    def test_is_funny_anyone(self):
        """ Anyone else tim should be funny """
        self.assertTrue(is_funny('blue'),'blue should be funny')
        self.assertTrue(is_funny('tammy'),'tammy should be funny')
        self.assertTrue(is_funny('sven'),'sven should be funny')

    def test_laugh(self):
        self.assertIn(laugh(),('lol','haha','tehehe'))
             
if __name__ == '__main__':
    unittest.main()