"""Module tests counting module"""
import unittest
from program.gaimsettings import GaimSettings
from program.counting import Counting
from program.shapes import Shapes

class TestCounting(unittest.TestCase):
    "The function tests the counting module"
    def setUp(self):
        self.pieces_1=[[0,680,100,20],[200,680,100,20],[300,680,100,20]]
        self.pieces_2=[[0,680,100,20],[200,680,100,20],[300,680,100,20], [100,680,100,20],[400,680,100,20]]

    def test_return_right_final_y(self):
        count=Counting()
        final_y_1=count.count_old_shapes(100,680,100,20,self.pieces_1)
        final_y_2=count.count_old_shapes(100,680,10020,self.pieces_2)

        self.assertEqual(final_y_1,680)
        self.assertEqual(final_y_2,660)