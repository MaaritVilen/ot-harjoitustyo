import unittest
from program.gaimsettings import GaimSettings

#Testataan että hakee tuloksen oikein
class TestGaimSettings(unittest.TestCase):
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