import unittest
import password_worker

class TestGeneratorPassword(unittest.TestCase):
    """Набор тестов для генератора пароля"""
    def test_len_password(self):
         self.assertEqual(len(password_worker.generatorPassword(len_password=10)), 10) 

    def test_valid_password(self):
        self.assertTrue(password_worker.passwordValidator(password_worker.generatorPassword()))

    
class TestPasswordValidationChecks(unittest.TestCase):
    """Проверка вспомогательных функций при генерации пароля"""

    def test_line_intersections_false(self):
        self.assertFalse(password_worker.checkingMatchingCharInStrings("123ggfte", "00_dsads"))

    def test_line_intersections_true(self):
        self.assertTrue(password_worker.checkingMatchingCharInStrings("123ggfte", "00_dsad12s"))

    def test_validator_password_true(self):
        self.assertTrue(password_worker.passwordValidator("_d)Fa4'#O5"))

    def test_validator_password_too_shot(self):
        self.assertFalse(password_worker.passwordValidator("_d)Fa4'#O5", minimal_len_password=100))

    def test_validator_password_dont_element(self):
        self.assertFalse(password_worker.passwordValidator("aa_oooooooooo"))
        self.assertFalse(password_worker.passwordValidator("1a_oooooooooo"))
        self.assertFalse(password_worker.passwordValidator("1A_OOOOOOOOOO"))
        self.assertFalse(password_worker.passwordValidator("1aAoooooooooo"))
