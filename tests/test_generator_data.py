import unittest
import generatot_test_data

class TestGeneratorPassword(unittest.TestCase):
    """Набор тестов для генератора пароля"""
    def test_len_password(self):
         self.assertEqual(len(generatot_test_data.generatorPassword(len_password=10)), 10) 

    def test_valid_password(self):
        self.assertTrue(generatot_test_data.passwordValidator(generatot_test_data.generatorPassword()))

    
class TestPasswordValidationChecks(unittest.TestCase):
    """Проверка вспомогательных функций при генерации пароля"""

    def test_line_intersections_false(self):
        self.assertFalse(generatot_test_data.checkingMatchingCharInStrings("123ggfte", "00_dsads"))

    def test_line_intersections_true(self):
        self.assertTrue(generatot_test_data.checkingMatchingCharInStrings("123ggfte", "00_dsad12s"))

    def test_validator_password_true(self):
        self.assertTrue(generatot_test_data.passwordValidator("_d)Fa4'#O5"))

    def test_validator_password_too_shot(self):
        self.assertFalse(generatot_test_data.passwordValidator("_d)Fa4'#O5", minimal_len_password=100))

    def test_validator_password_dont_element(self):
        self.assertFalse(generatot_test_data.passwordValidator("aa_oooooooooo"))
        self.assertFalse(generatot_test_data.passwordValidator("1a_oooooooooo"))
        self.assertFalse(generatot_test_data.passwordValidator("1A_OOOOOOOOOO"))
        self.assertFalse(generatot_test_data.passwordValidator("1aAoooooooooo"))
