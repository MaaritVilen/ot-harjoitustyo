"""Module tests functionin of saving result and retrieving old results"""
import unittest
from gaimsettings import GaimSettings
from counting import Counting
#from shapes import Shapes

class TestGaimSettings(unittest.TestCase):
    """Class tests """
    def setUp(self):
        print("no need")

    def test_can_return_result(self):
        game=GaimSettings()
        result=game.previous_results("maarit")

        self.assertEqual(result,10)

#Testataan että tallentaa ja hakee tuloksen oikein
    
    def test_can_save_and_return_result_for_lower_result(self):
        game=GaimSettings()
        game.save_result("olli",17)
        game.save_result("olli",13)
        result=game.previous_results("olli")
        self.assertEqual(result,17)
    
class TestCounting(unittest.TestCase):
    def setUp(self):
        print("no need")

    def test_move_right_is_right(self):
        count_move=Counting()
        x1=count_move.count_x(100, 50, 0, 5)
        self.assertEqual(x1,105)
        x2=count_move.count_x(400, 100, 0, 5)
        self.assertEqual(x2,400)
    
    def test_move_left_is_right(self):
        count_move=Counting()
        x3=count_move.count_x(100, 50, -5, 0)
        self.assertEqual(x3,95)
        x4=count_move.count_x(0, 50, -5, 0)
        self.assertEqual(x4,0)
    
    def test_move_down_is_right(self):
        count_move=Counting()
        y1=count_move.count_y(50,50)
        self.assertEqual(y1, 51)
        y2=count_move.count_y(600, 100)
        self.assertEqual(y2,600)