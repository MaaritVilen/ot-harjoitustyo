import unittest
import pygame
from mainbody import MainBody

class TestMain(unittest.TestCase):
    def test_can_move_stage_1(self):
        game=MainBody()
        game.main()
        pygame.KEYDOWN, pygame.K_RETURN

        self.assertEqual(game.gamestatus,1)