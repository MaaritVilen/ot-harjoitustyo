import unittest
import pygame
from mainbody import MainBody

class TestMainBody(unittest.TestCase):
    def setUp(self):
        print("no need")

    def test_can_move_stage_1(self):
        game=MainBody()
        game.main()
        #pygame.event.type==pygame.KEYDOWN
        #pygame.event.key==pygame.K_RETURN

        self.assertEqual(game.gamestatus,1)